"""Offline checks for the hallucination guard (no API key needed).  Run:  python test_guard.py"""

from lawyer_core import check_answer, language_issue, lawyer_reasons, load_kb

_, verified = load_kb()
BY_ID = {e["id"]: e for e in verified}

# (description, answer text, should the guard flag it?)
CASES = [
    ("allowed facts", "Call the National Consumer Helpline on 1915 or 1800-11-4000 [KB:NCH]. District Commission "
     "handles up to Rs 50 lakh under Section 34(1) [KB:CPA-JURIS-MONEY]. You paid Rs 2,499 on 2 September 2026.", False),
    ("emergency number", "Please call 112 immediately.", False),
    ("Hindi helpline", "राष्ट्रीय उपभोक्ता हेल्पलाइन 1915 पर कॉल करें [KB:NCH]", False),
    ("invented section", "Under Section 72 the seller must pay 18% interest.", True),
    ("invented section in Hindi", "धारा 35 के तहत शिकायत करें।", True),
    ("invented case law", "In Amazon Seller Services v. Rahul Sharma (2021) the commission ordered a refund.", True),
    ("unknown source tag", "You get 18% interest on late refunds [KB:CPA-INTEREST].", True),
    ("newly verified facts", "File within two years [KB:CPA-LIMITATION] under Section 69, at the commission where you live (Section 34(2)) [KB:CPA-WHERE]. WhatsApp 8800001915 [KB:NCH].", False),
    ("invented helpline", "You can also call the consumer helpline 1800-180-4566.", True),
    # added after the first test run (v1 failures)
    ("invented website", "File online at ejagriti.gov.in [KB:EJAGRITI].", True),
    ("verified website", "Register at consumerhelpline.gov.in [KB:NCH].", False),
    ("legal conclusion", "Aap replacement paane ke haqdaar hain under the Act [KB:CPA-ACT].", True),
    ("legal conclusion 2", "Refusing a refund amounts to unfair trade practice.", True),
    ("price is not a phone number", '"product": "Mobile phone", "amount_paid": "Rs 18000"', False),
]

# (description, what the user said, should the code demand a real lawyer?)
LAWYER_CASES = [
    ("Rs 85 lakh flat", "A builder took Rs 85 lakh for a flat in 2026.", True),
    ("Rs 1.2 crore", "I paid 1.2 crore for a villa last month.", True),
    ("3 years old", "I bought a washing machine 3 years ago and it has been faulty.", True),
    ("year 2022", "I paid the builder in 2022 and still no flat.", True),
    ("small recent case", "I ordered shoes on 2 September 2026 for Rs 2,499.", False),
    ("Rs 40,000 deposit", "My landlord kept my Rs 40,000 deposit.", False),
]

# (description, question, answer, should it be flagged as the wrong language?)
LANGUAGE_CASES = [
    ("English -> Hindi (v1 T06)", "The shopkeeper threatened me. I'm scared.", "कृपया तुरंत 112 पर कॉल करें।", True),
    ("Hindi -> Hindi", "मेरा रिफंड नहीं आया।", "कृपया अपना ऑर्डर नंबर बताइए।", False),
    ("Tamil -> English", "நான் என்ன செய்ய வேண்டும்?", "Please tell me the seller's name.", True),
    ("Hinglish -> Hinglish", "Mera refund nahi aaya, kya karu?", "Aap pehle grievance officer ko mail karein.", False),
]


if __name__ == "__main__":
    failures = 0
    for name, text, should_flag in CASES:
        issues = check_answer(text, BY_ID)
        ok = bool(issues) == should_flag
        failures += not ok
        print(f"{'PASS' if ok else 'FAIL'}  {name}  ->  {issues or 'no issues'}")
    for name, text, should_flag in LAWYER_CASES:
        reasons = lawyer_reasons(text, this_year=2026)
        ok = bool(reasons) == should_flag
        failures += not ok
        print(f"{'PASS' if ok else 'FAIL'}  lawyer rule: {name}  ->  {reasons or 'no lawyer needed'}")
    for name, q, a, should_flag in LANGUAGE_CASES:
        issue = language_issue(q, a)
        ok = bool(issue) == should_flag
        failures += not ok
        print(f"{'PASS' if ok else 'FAIL'}  language: {name}  ->  {issue or 'same language'}")
    total = len(CASES) + len(LAWYER_CASES) + len(LANGUAGE_CASES)
    print(f"\n{total - failures}/{total} passed")
    raise SystemExit(1 if failures else 0)
