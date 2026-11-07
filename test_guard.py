"""Offline checks for the hallucination guard (no API key needed).  Run:  python test_guard.py"""

from lawyer_core import check_answer, load_kb

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
]

if __name__ == "__main__":
    failures = 0
    for name, text, should_flag in CASES:
        issues = check_answer(text, BY_ID)
        ok = bool(issues) == should_flag
        failures += not ok
        print(f"{'PASS' if ok else 'FAIL'}  {name}  ->  {issues or 'no issues'}")
    print(f"\n{len(CASES) - failures}/{len(CASES)} passed")
    raise SystemExit(1 if failures else 0)
