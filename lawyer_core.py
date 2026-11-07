"""Core logic for AI Lawyer, an AI helper for consumer problems in India.

Everything the app and the test runner share lives here:
- loading the verified law file (knowledge_base.json)
- the prompts
- calls to the model (Gemini by default, swappable via MODEL_NAME)
- the hallucination guard that checks every answer before the user sees it
"""

import json
import os
import re
import time
from pathlib import Path

from google import genai
from google.genai import types

# ---- Config: change the model here or via the MODEL_NAME env variable ----
MODEL_NAME = os.environ.get("MODEL_NAME", "gemini-3.8-flash")
# Backup models tried in order if the main one is busy (503) or out of free quota (429)
FALLBACK_MODELS = [m.strip() for m in os.environ.get("FALLBACK_MODELS", "gemini-3.6-flash,gemini-3.5-flash-lite").split(",") if m.strip()]
TEMPERATURE = 0.2  # low = fewer creative (made-up) answers
# temporary problems on Google's side: wait and retry, then try a backup model
BUSY_SIGNS = ("500", "INTERNAL", "503", "UNAVAILABLE", "504", "DEADLINE_EXCEEDED", "429", "RESOURCE_EXHAUSTED",
              "overloaded", "high demand", "timed out", "Timeout", "timeout", "ReadTimeout", "ConnectError")

KB_PATH = Path(__file__).parent / "knowledge_base.json"


# ---------------------------------------------------------------- knowledge
def load_kb(path=KB_PATH):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    verified = [e for e in data["entries"] if e.get("status") == "verified"]
    return data, verified


def kb_as_text(verified):
    lines = []
    for e in verified:
        lines.append(
            f"[KB:{e['id']}] {e['title']}\n"
            f"  Law: {e['law']} | Section: {e['section']}\n"
            f"  Meaning: {e['plain']}"
        )
    return "\n\n".join(lines)


# ---------------------------------------------------------------- prompts
def system_prompt(data, verified):
    return f"""You are AI Lawyer, a friendly legal helper for ordinary people in India.
You ONLY help with consumer problems: {data['scope']}

HOW TO TALK
- Reply ONLY in the language of the question the user has just asked, in the same script. English question ->
  English answer (no Hindi or Hinglish words). Hindi question -> Hindi. Hinglish -> Hinglish. Tamil -> Tamil.
  If the user switches language, switch with them.
- Use simple words. Short paragraphs. No legal jargon without explaining it.
- Be warm. People who come to you are often stressed.

WHAT TO DO
1. Understand the problem. If key facts are missing (what was bought, from whom, when, how much was paid,
   what went wrong, what proof they have, what they want), ask for them. Ask at most 3 questions at a time.
2. When you have enough facts, explain where they stand and the options, cheapest and simplest first:
   contact the seller's grievance officer -> National Consumer Helpline -> legal notice -> consumer commission.
3. Offer to build their case file and draft a legal notice (they can click the buttons in the app).

STRICT RULES ABOUT LAW (most important)
- You may ONLY mention laws, sections, rules, deadlines, amounts, phone numbers and portals that appear in
  the VERIFIED SOURCES below. Every time you use one, put its tag right after, like [KB:NCH].
- NEVER mention any section number, case name, court judgment, deadline or fee that is not in the verified
  sources, even if you think you know it. Instead say: "I am not sure about this; please confirm with a
  lawyer or the National Consumer Helpline."
- Never promise an outcome ("you will surely win", "you will get compensation").
- If the problem is outside your scope ({', '.join(data['out_of_scope'])}), say clearly that you cannot
  help with that and suggest they consult a lawyer or their District Legal Services Authority for free legal aid.
- Never state a legal conclusion that is not written in the verified sources, such as "you are entitled to a
  replacement", "this is an unfair trade practice" or "their policy is illegal". Say "you may have a claim" and
  let the consumer commission or a lawyer decide.
- Never give a website address, email or phone number unless it is written in the verified sources.
- Recommend a real lawyer, clearly and early, when: the amount paid is above Rs 50 lakh; the problem may be
  more than two years old (the filing deadline may have passed); the other side has started legal action; or
  there is a criminal angle. Say why.
- If someone is in danger or facing a threat or a crime, tell them to call 112 immediately.
- Always end advice with one line reminding them this is general information, not a lawyer's advice.

VERIFIED SOURCES
{kb_as_text(verified)}
"""


CASE_FILE_SCHEMA = {
    "type": "object",
    "properties": {
        "summary": {"type": "string"},
        "in_scope": {"type": "boolean"},
        "consumer_name": {"type": "string"},
        "opposite_party": {"type": "string"},
        "product_or_service": {"type": "string"},
        "amount_paid": {"type": "string"},
        "timeline": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {"date": {"type": "string"}, "event": {"type": "string"}},
                "required": ["date", "event"],
            },
        },
        "evidence_have": {"type": "array", "items": {"type": "string"}},
        "evidence_missing": {"type": "array", "items": {"type": "string"}},
        "what_they_want": {"type": "string"},
        "next_steps": {"type": "array", "items": {"type": "string"}},
        "needs_real_lawyer": {"type": "boolean"},
        "lawyer_reason": {"type": "string"},
    },
    "required": [
        "summary", "in_scope", "timeline", "evidence_have",
        "evidence_missing", "next_steps", "needs_real_lawyer",
    ],
}

CASE_FILE_INSTRUCTION = """From the conversation so far, build a case file in English.
- Use ONLY facts the user actually said. Do not add legal conclusions (like "entitled" or "unfair trade practice"). If a fact is unknown, write "not provided". Never invent dates or amounts.
- timeline: every dated event in order. Use the user's own date wording if exact dates are unknown.
- evidence_missing: proof that would help but the user has not mentioned (bill, order ID, screenshots, emails...).
- next_steps: simple actions in order. Only mention helplines/portals from the verified sources, with [KB:ID] tags.
- needs_real_lawyer: true if the matter is outside consumer scope, the amount paid is above Rs 50 lakh, the
  problem may be more than two years old, it has a criminal angle, or the other side has started legal action.
  Give the reason in lawyer_reason."""

NOTICE_INSTRUCTION = """Draft a short legal notice from the consumer to the opposite party, based ONLY on the case file below.
- Plain, polite, firm English. Address to the company / its grievance officer.
- Include: facts with dates, what went wrong, what the consumer demands (refund/replacement/compensation as
  per what_they_want), and a deadline of 15 days to respond, after which the consumer may approach the
  National Consumer Helpline and the consumer commission.
- You may reference ONLY laws in the verified sources, with [KB:ID] tags. No other sections or cases.
- Do not state legal conclusions that are not in the verified sources (for example "unfair trade practice",
  "entitled to", "illegal"). Describe the facts and the demand instead.
- No website addresses, emails or phone numbers except those written in the verified sources.
- Use placeholders like [Your full address] for anything not in the case file. Never invent facts.
- Do not add a lawyer's name or signature. It is sent by the consumer personally.

CASE FILE:
{case_file}"""


# ---------------------------------------------------------------- model calls
class Lawyer:
    def __init__(self, api_key, model_name=MODEL_NAME, kb_path=KB_PATH):
        # timeout is in milliseconds: a call that hangs gives up after 120 s and is retried
        self.client = genai.Client(api_key=api_key, http_options=types.HttpOptions(timeout=120_000))
        self.model = model_name
        self.last_model_used = model_name
        self.data, self.verified = load_kb(kb_path)
        self.sys = system_prompt(self.data, self.verified)
        self.by_id = {e["id"]: e for e in self.verified}

    def _generate(self, contents, config=None):
        """Call the model. If it is busy, retry twice, then try the backup models.
        Records which model actually answered in self.last_model_used."""
        models = [self.model] + [m for m in FALLBACK_MODELS if m != self.model]
        last_err = None
        for model in models:
            for attempt in range(3):
                try:
                    resp = self.client.models.generate_content(model=model, contents=contents, config=config)
                    self.last_model_used = model
                    return resp.text or ""
                except Exception as e:
                    last_err = e
                    msg = str(e)
                    if "404" in msg or "NOT_FOUND" in msg:
                        break  # this model name does not exist -> try the next model
                    if not any(s in msg for s in BUSY_SIGNS):
                        raise  # a real error (bad key etc.), show it
                    time.sleep(2 + 3 * attempt)
        raise last_err

    def _call(self, contents, json_schema=None, extra_system=""):
        cfg = dict(system_instruction=self.sys + extra_system, temperature=TEMPERATURE)
        if json_schema:
            cfg["response_mime_type"] = "application/json"
            cfg["response_schema"] = json_schema
        return self._generate(contents, types.GenerateContentConfig(**cfg))

    @staticmethod
    def to_contents(history):
        """history: list of {"role": "user"|"assistant", "text": str, "audio": bytes|None}"""
        contents = []
        for m in history:
            parts = []
            if m.get("audio"):
                parts.append(types.Part.from_bytes(data=m["audio"], mime_type=m.get("mime", "audio/wav")))
            if m.get("text"):
                parts.append(types.Part(text=m["text"]))
            role = "model" if m["role"] == "assistant" else "user"
            contents.append(types.Content(role=role, parts=parts))
        return contents

    def transcribe(self, audio_bytes, mime="audio/wav"):
        """Turn a voice note into text (any Indian language) so it can be shown and saved."""
        part = types.Part.from_bytes(data=audio_bytes, mime_type=mime)
        text = self._generate(
            [part, "Transcribe this voice note exactly, in the language spoken. Output only the transcript."]
        )
        return text.strip()

    def reply(self, history):
        """Chat answer, checked by the guard. If the guard finds problems, ask the model once to fix them."""
        answer = self._call(self.to_contents(history))
        question = next((m.get("text", "") for m in reversed(history) if m["role"] == "user"), "")
        issues = check_answer(answer, self.by_id)
        lang = language_issue(question, answer)
        if lang:
            issues = issues + [lang]
        retried = False
        if issues:
            retried = True
            fix = (
                "\n\nYOUR PREVIOUS DRAFT BROKE THE RULES: " + "; ".join(issues)
                + ". Rewrite it without those references. If you need that information, say you are not sure."
            )
            answer = self._call(self.to_contents(history), extra_system=fix)
            issues = check_answer(answer, self.by_id)
            lang = language_issue(question, answer)
            if lang:
                issues = issues + [lang]
        reasons = lawyer_reasons(user_text(history))
        already = any(LAWYER_NOTE_MARK in m.get("text", "") for m in history if m["role"] == "assistant")
        if reasons and not already:
            answer += f"\n\n{LAWYER_NOTE_MARK} **Please talk to a real lawyer:** " + "; ".join(reasons) + "."
        return {"text": answer, "issues": issues, "retried": retried, "sources": cited_sources(answer, self.by_id),
                "model_used": self.last_model_used, "lawyer_flags": reasons}

    def _case_json(self, contents, extra_system=""):
        raw = self._call(contents, json_schema=CASE_FILE_SCHEMA, extra_system=extra_system)
        try:
            return json.loads(raw)
        except json.JSONDecodeError:
            return {"error": "model did not return valid JSON", "raw": raw}

    def case_file(self, history):
        contents = self.to_contents(history) + [types.Content(role="user", parts=[types.Part(text=CASE_FILE_INSTRUCTION)])]
        cf = self._case_json(contents)
        first_issues = check_answer(json.dumps(cf, ensure_ascii=False), self.by_id)
        if first_issues:  # one rewrite, like the chat
            fix = ("\n\nYOUR PREVIOUS DRAFT BROKE THE RULES: " + "; ".join(first_issues)
                   + ". Rewrite the case file without those statements or references.")
            cf = self._case_json(contents, extra_system=fix)
        reasons = lawyer_reasons(user_text(history) + " " + str(cf.get("amount_paid", "")))
        if reasons and "error" not in cf:
            cf["needs_real_lawyer"] = True
            old = cf.get("lawyer_reason", "")
            keep = old if old and old.lower() not in ("not provided", "not applicable", "") else ""
            cf["lawyer_reason"] = "; ".join([r[0].upper() + r[1:] for r in reasons] + ([keep] if keep else []))
        issues = check_answer(json.dumps(cf, ensure_ascii=False), self.by_id)
        return {"case_file": cf, "issues": issues, "lawyer_flags": reasons}

    def legal_notice(self, case_file):
        prompt = NOTICE_INSTRUCTION.format(case_file=json.dumps(case_file, indent=2, ensure_ascii=False))
        contents = [types.Content(role="user", parts=[types.Part(text=prompt)])]
        text = self._call(contents)
        issues = check_answer(text, self.by_id)
        retried = False
        if issues:
            retried = True
            fix = ("\n\nYOUR PREVIOUS DRAFT BROKE THE RULES: " + "; ".join(issues)
                   + ". Rewrite the notice without those statements or references.")
            text = self._call(contents, extra_system=fix)
            issues = check_answer(text, self.by_id)
        return {"text": text, "issues": issues, "retried": retried, "sources": cited_sources(text, self.by_id)}


# ---------------------------------------------------------------- the guard
SECTION_RE = re.compile(r"\b(?:section|sec\.?|धारा)\s*(\d+[A-Za-z]?(?:\s*\(\s*[0-9a-z]+\s*\))*)", re.IGNORECASE)
TAG_RE = re.compile(r"\[KB:([A-Z0-9\-]+)\]")
# A court case citation: "X v. Y" / "X vs Y" followed soon by a year or a law-report name
CASE_RE = re.compile(
    r"\b[A-Z][\w.&]*(?:\s[A-Z][\w.&]*)*\s+(?:v\.|vs\.?|versus)\s+[A-Z][\w.&]*(?:\s[A-Z][\w.&]*)*"
    r"[^.\n]{0,40}?(?:\(?(?:19|20)\d\d\)?|AIR|SCC|CPJ|SCR)",
    re.UNICODE,
)
# Only numbers that are presented as something to call / message
PHONE_RE = re.compile(
    r"(?:call|dial|helpline|toll[- ]?free|phone|number|whatsapp|sms|फ़ोन|फोन|कॉल|नंबर|हेल्पलाइन)"
    r"\D{0,25}?(\+?\d[\d\- ]{2,15}\d)",
    re.IGNORECASE,
)


# A web address: anything like name.gov.in, name.nic.in, name.com ...
URL_RE = re.compile(r"\b((?:[a-z0-9-]+\.)+(?:gov\.in|nic\.in|co\.in|org\.in|in|com|org|net))\b", re.IGNORECASE)
# Legal conclusions the verified file does not support
CLAIM_RE = re.compile(r"\b(entitled|haqdaar|hakdaar|unfair trade practice)\b|हकदार|हक़दार", re.IGNORECASE)
MONEY_NEAR_RE = re.compile(r"rs\.?|₹|rupee|rupay|inr|रुपये", re.IGNORECASE)


def _digits(s):
    return re.sub(r"\D", "", s)


def _norm_section(s):
    return re.sub(r"\s+", "", s).lower()


def allowed_sections(by_id):
    allowed = set()
    for e in by_id.values():
        for m in re.finditer(r"\d+[A-Za-z]?(?:\(\s*[0-9a-z]+\s*\))*", e["section"]):
            allowed.add(_norm_section(m.group(0)))
    return allowed


def allowed_numbers(by_id):
    text = " ".join(e["plain"] for e in by_id.values())
    return {_digits(n) for n in re.findall(r"\+?\d[\d\- ]*\d", text)}


def allowed_sites(by_id):
    sites = set()
    for e in by_id.values():
        for m in URL_RE.finditer(e["plain"] + " " + e["source"]):
            sites.add(m.group(1).lower().removeprefix("www."))
    return sites


# ---------------------------------------------------------------- lawyer rule (code, not the model)
LAWYER_NOTE_MARK = "⚖️"
AMOUNT_RE = re.compile(r"(\d+(?:[.,]\d+)?)\s*(lakhs?|lacs?|crores?|cr\b|लाख|करोड़|करोड)", re.IGNORECASE)
RUPEES_RE = re.compile(r"(?:rs\.?|₹|inr)\s*([\d,]{7,})|([\d,]{7,})\s*(?:rs|rupees|रुपये)", re.IGNORECASE)
YEARS_AGO_RE = re.compile(r"(\d+)\s*(?:years?|yrs?|saal|sal|वर्ष|साल)\s*(?:ago|pehle|pahle|पहले|purana|old)?", re.IGNORECASE)
YEAR_RE = re.compile(r"\b(19\d\d|20\d\d)\b")


SCRIPTS = {"Devanagari": (0x0900, 0x097F), "Tamil": (0x0B80, 0x0BFF), "Bengali": (0x0980, 0x09FF),
           "Telugu": (0x0C00, 0x0C7F), "Kannada": (0x0C80, 0x0CFF), "Malayalam": (0x0D00, 0x0D7F),
           "Gujarati": (0x0A80, 0x0AFF), "Gurmukhi": (0x0A00, 0x0A7F), "Odia": (0x0B00, 0x0B7F)}


def main_script(text):
    """The writing system most letters in the text use: 'Latin' (English/Hinglish) or an Indian script."""
    counts = {"Latin": sum(c.isascii() and c.isalpha() for c in text)}
    for name, (lo, hi) in SCRIPTS.items():
        counts[name] = sum(lo <= ord(c) <= hi for c in text)
    return max(counts, key=counts.get) if any(counts.values()) else "Latin"


def language_issue(question, answer):
    q, a = main_script(question), main_script(answer)
    if q != a:
        return f"the question is written in {q} script but you answered in {a} script; answer in the question's language"
    return None


def user_text(history):
    return " ".join(m.get("text", "") for m in history if m["role"] == "user")


def largest_amount(text):
    vals = []
    for num, unit in AMOUNT_RE.findall(text):
        n = float(num.replace(",", "."))
        vals.append(n * (1e7 if unit.lower().startswith(("cr", "कर")) else 1e5))
    for a, b in RUPEES_RE.findall(text):
        vals.append(float((a or b).replace(",", "")))
    return max(vals, default=0)


def lawyer_reasons(text, this_year=None):
    """Reasons a real lawyer is needed, decided by code from what the user said."""
    import datetime
    this_year = this_year or datetime.date.today().year
    reasons = []
    if largest_amount(text) > 50e5:
        reasons.append("the amount is above Rs 50 lakh, so the case goes to the State or National Commission")
    years = [int(n) for n in YEARS_AGO_RE.findall(text)] + [this_year - int(y) for y in YEAR_RE.findall(text)]
    if any(y >= 2 for y in years):
        reasons.append("the problem may be more than two years old, so the filing deadline may have passed [KB:CPA-LIMITATION]")
    return reasons


def check_answer(text, by_id):
    """Return a list of problems: unknown source tags, section numbers or case names not in the verified file,
    and helpline-style numbers that are not in the verified file."""
    issues = []
    for tag in set(TAG_RE.findall(text)):
        if tag not in by_id:
            issues.append(f"cited unknown source [KB:{tag}]")

    ok_sections = allowed_sections(by_id)
    for m in SECTION_RE.finditer(text):
        sec = _norm_section(m.group(1))
        base = re.match(r"\d+[a-z]?", sec).group(0)
        if sec not in ok_sections and base not in {re.match(r'\d+[a-z]?', s).group(0) for s in ok_sections}:
            issues.append(f"mentioned 'Section {m.group(1).strip()}' which is not in the verified sources")

    for m in CASE_RE.finditer(text):
        issues.append(f"mentioned a court case '{m.group(0)}' which is not in the verified sources")

    ok_sites = allowed_sites(by_id)
    for m in URL_RE.finditer(text):
        site = m.group(1).lower().removeprefix("www.")
        if not any(site == ok or site.endswith("." + ok) or ok.endswith("." + site) for ok in ok_sites):
            issues.append(f"mentioned the website '{m.group(1)}' which is not in the verified sources")

    for m in CLAIM_RE.finditer(text):
        issues.append(f"stated a legal conclusion ('{m.group(0)}') that is not in the verified sources")

    ok_nums = allowed_numbers(by_id) | {"112"}  # 112 = national emergency number
    for m in PHONE_RE.finditer(text):
        if MONEY_NEAR_RE.search(m.group(0)):
            continue  # "phone ... Rs 18000" is a price, not a phone number
        num = _digits(m.group(1))
        if len(num) >= 3 and num not in ok_nums:
            issues.append(f"mentioned the phone number '{m.group(1).strip()}' which is not in the verified sources")
    return sorted(set(issues))


def cited_sources(text, by_id):
    seen = []
    for tag in TAG_RE.findall(text):
        if tag in by_id and tag not in seen:
            seen.append(tag)
    return [{"id": t, "title": by_id[t]["title"], "url": by_id[t]["source"]} for t in seen]
