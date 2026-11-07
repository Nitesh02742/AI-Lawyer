"""Run every test case through the same pipeline as the app and save unedited outputs.

Usage:
    export GEMINI_API_KEY=...          (Windows: set GEMINI_API_KEY=...)
    python run_tests.py                 # all tests
    python run_tests.py T07_trick_section T08_trick_case_law   # only some
Outputs go to outputs/<run time>/ : one .json and one readable .md per test, plus summary.csv
"""

import csv
import json
import os
import sys
import time
from datetime import datetime
from pathlib import Path

from lawyer_core import MODEL_NAME, Lawyer

PAUSE_SECONDS = float(os.environ.get("PAUSE_SECONDS", "4"))  # stay under free-tier rate limits


def call_with_retry(fn, *args, tries=3):
    for i in range(tries):
        try:
            return fn(*args)
        except Exception as e:  # rate limit or network blip
            print(f"   error: {str(e)[:120]}", flush=True)
            if "API key not valid" in str(e) or "API_KEY_INVALID" in str(e):
                sys.exit("\nSTOPPED: your API key is not valid. Check the 'set GEMINI_API_KEY=' line "
                         "(only the key after '=', no extra words, spaces or quotes), then run again.\n"
                         "Delete the incomplete folder this run created inside 'outputs'.")
            if i == tries - 1:
                return {"error": str(e)}
            print(f"   waiting {20 * (i + 1)} s, then retrying ...", flush=True)
            time.sleep(20 * (i + 1))


def run_case(lawyer, case):
    history, transcript = [], []
    for n, turn in enumerate(case["turns"], 1):
        history.append({"role": "user", "text": turn})
        print(f"   turn {n}: asking the model ...", flush=True)
        res = call_with_retry(lawyer.reply, history)
        print(f"   turn {n}: got an answer ({res.get('model_used') or 'error'})", flush=True)
        time.sleep(PAUSE_SECONDS)
        answer = res.get("text", f"[ERROR] {res.get('error')}")
        history.append({"role": "assistant", "text": answer})
        transcript.append({"user": turn, "assistant": answer, "guard_issues": res.get("issues", []),
                           "guard_retried": res.get("retried", False), "sources": res.get("sources", []),
                           "model_used": res.get("model_used")})

    out = {"id": case["id"], "type": case["type"], "expect": case["expect"], "model": lawyer.model,
           "transcript": transcript}
    if case.get("build_case_file"):
        print("   building case file ...", flush=True)
        out["case_file"] = call_with_retry(lawyer.case_file, history)
        time.sleep(PAUSE_SECONDS)
        if case.get("draft_notice") and "case_file" in out["case_file"]:
            print("   drafting legal notice ...", flush=True)
            out["legal_notice"] = call_with_retry(lawyer.legal_notice, out["case_file"]["case_file"])
            time.sleep(PAUSE_SECONDS)
    return out


def to_markdown(o):
    md = [f"# {o['id']}  ({o['type']})", f"**Model set:** {o['model']} (each answer below shows which model actually replied)", f"**Expected:** {o['expect']}", ""]
    for i, t in enumerate(o["transcript"], 1):
        md += [f"## Turn {i}", f"**User:** {t['user']}", "", f"**AI Lawyer:**\n\n{t['assistant']}", ""]
        md.append(f"_Model used: {t.get('model_used')} | guard issues: {t['guard_issues'] or 'none'} | retried: {t['guard_retried']}_\n")
    if "case_file" in o:
        md += ["## Case file", "```json", json.dumps(o["case_file"], indent=2, ensure_ascii=False), "```"]
    if "legal_notice" in o:
        md += ["## Legal notice", o["legal_notice"].get("text", str(o["legal_notice"])),
               f"\n_Guard issues: {o['legal_notice'].get('issues') or 'none'}_"]
    md += ["", "## Manual review (fill in by hand)", "- Verdict (good / partly / bad):", "- Notes:"]
    return "\n".join(md)


def main():
    key = os.environ.get("GEMINI_API_KEY")
    if not key:
        sys.exit("Set GEMINI_API_KEY first.")
    lawyer = Lawyer(api_key=key, model_name=os.environ.get("MODEL_NAME", MODEL_NAME))
    cases = json.loads(Path("test_cases.json").read_text(encoding="utf-8"))
    if len(sys.argv) > 1:
        cases = [c for c in cases if c["id"] in sys.argv[1:]]

    out_dir = Path("outputs") / datetime.now().strftime("%Y%m%d_%H%M%S")
    out_dir.mkdir(parents=True, exist_ok=True)
    # the brief asks for the test cases to be included with the raw outputs
    (out_dir / "test_cases.json").write_text(Path("test_cases.json").read_text(encoding="utf-8"), encoding="utf-8")
    rows = []
    for c in cases:
        print(f"Running {c['id']} ...", flush=True)
        o = run_case(lawyer, c)
        (out_dir / f"{c['id']}.json").write_text(json.dumps(o, indent=2, ensure_ascii=False), encoding="utf-8")
        (out_dir / f"{c['id']}.md").write_text(to_markdown(o), encoding="utf-8")
        issues = sum(len(t["guard_issues"]) for t in o["transcript"])
        retried = any(t["guard_retried"] for t in o["transcript"])
        cf = o.get("case_file", {}).get("case_file", {}) if isinstance(o.get("case_file"), dict) else {}
        rows.append({"id": c["id"], "type": c["type"], "guard_retried": retried,
                     "guard_issues_left": issues,
                     "needs_real_lawyer": cf.get("needs_real_lawyer", "") if cf else "",
                     "manual_verdict": "", "notes": ""})

    with open(out_dir / "summary.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f"\nDone. Outputs saved in {out_dir}")


if __name__ == "__main__":
    main()
