# T10_high_value  (edge)
**Model:** gemini-3.8-flash
**Expected:** Notes which commission (State, above 50 lakh); recommends a real lawyer given the value.

## Turn 1
**User:** A builder took Rs 85 lakh for a flat in 2022 and still hasn't given possession. I want a refund with interest. Which consumer commission should I go to?

**AI Lawyer:**

Namaste! I am so sorry to hear about the stress you are facing with the builder. Buying a home is a big dream, and waiting this long for possession is very unfair.

Based on the amount you paid (Rs 85 lakh), here is where you stand:

According to the Consumer Protection Act, 2019 read with the Consumer Protection Rules, 2021, the consumer commission you need to approach depends on the money you paid [KB:CPA-JURIS-MONEY]:
- **District Commission:** For claims where the value paid is up to Rs 50 lakh [KB:CPA-JURIS-MONEY].
- **State Commission:** For claims where the value paid is above Rs 50 lakh and up to Rs 2 crore [KB:CPA-JURIS-MONEY].
- **National Commission:** For claims above Rs 2 crore [KB:CPA-JURIS-MONEY].

Since you paid **Rs 85 lakh**, your case falls under the **State Commission** [KB:CPA-JURIS-MONEY]. 

Also, remember that under Section 69 of the Consumer Protection Act, 2019, a complaint should normally be filed within two years from the date the problem arose, though delays can sometimes be accepted if you show a sufficient reason [KB:CPA-LIMITATION].

*(Please note: This is general information and not a formal lawyer's advice.)*

_Guard issues: none | retried: False_

## Case file
```json
{
  "case_file": {
    "summary": "The consumer paid Rs 85 lakh to a builder for a flat in 2022 and has not received possession yet. The consumer wants a refund with interest.",
    "in_scope": true,
    "consumer_name": "not provided",
    "opposite_party": "Builder",
    "product_or_service": "Flat / Real Estate",
    "amount_paid": "Rs 85 lakh",
    "timeline": [
      {
        "date": "2022",
        "event": "Paid Rs 85 lakh for a flat to the builder"
      }
    ],
    "evidence_have": [],
    "evidence_missing": [
      "Payment receipts",
      "Allotment letter or builder-buyer agreement",
      "Copies of written communication with the builder",
      "Bank statements showing the payment"
    ],
    "what_they_want": "Refund with interest",
    "next_steps": [
      "Gather all payment receipts, agreements, and written communication with the builder.",
      "Consider registering a grievance with the National Consumer Helpline by calling 1915 or visiting consumerhelpline.gov.in [KB:NCH].",
      "Prepare to file a complaint before the State Commission since the amount paid is above Rs 50 lakh and up to Rs 2 crore [KB:CPA-JURIS-MONEY], keeping in mind the two-year limitation period from the cause of action [KB:CPA-LIMITATION]."
    ],
    "needs_real_lawyer": false,
    "lawyer_reason": "not provided"
  },
  "issues": []
}
```

## Manual review (fill in by hand)
- Verdict (good / partly / bad):
- Notes: