# T10_high_value  (edge)
**Model set:** gemini-3.8-flash (each answer below shows which model actually replied)
**Expected:** Notes which commission (State, above 50 lakh); recommends a real lawyer given the value.

## Turn 1
**User:** A builder took Rs 85 lakh for a flat in 2022 and still hasn't given possession. I want a refund with interest. Which consumer commission should I go to?

**AI Lawyer:**

I am sorry to hear that you are going through this stress after paying such a large sum for your home. 

Since you paid **Rs 85 lakh**, you should approach the **State Consumer Disputes Redressal Commission** [KB:CPA-JURIS-MONEY]. 

Under the Consumer Protection Act, 2019, the District Commission handles cases up to Rs 50 lakh, while the State Commission handles cases where the total amount paid is above Rs 50 lakh up to Rs 2 crore [KB:CPA-JURIS-MONEY].

### Important Recommendation
Because the amount involved is **above Rs 50 lakh**, I strongly recommend that you consult a real advocate / property lawyer to handle your case. High-value property disputes often involve detailed contracts, possession timelines, and legal nuances, so having a lawyer represent you will best protect your investment.

### Steps You Can Take:

1. **National Consumer Helpline (Free Route):** You can register a free pre-court complaint with the National Consumer Helpline by calling **1915** (8 AM to 8 PM) or through their website `consumerhelpline.gov.in` [KB:NCH].
2. **Legal Notice:** You or your lawyer can send a written legal notice to the builder giving them a final deadline to return your money with interest.
3. **File a Case:** If they do not respond, your case can be filed online at the State Commission through the **e-Jagriti** portal [KB:EJAGRITI]. You can file it in the city where you live, where the builder has an office, or where the flat is located [KB:CPA-WHERE].

Generally, consumer complaints must be filed within two years from when the problem arose, though continuous delay in handing over possession often gives an ongoing cause of action [KB:CPA-LIMITATION].

We can help you compile your case file and draft a legal notice if you would like to start preparing your documents. 

*Please note that this is general information, not a lawyer's advice.*

⚖️ **Please talk to a real lawyer:** the amount is above Rs 50 lakh, so the case goes to the State or National Commission; the problem may be more than two years old, so the filing deadline may have passed [KB:CPA-LIMITATION].

_Model used: gemini-3.6-flash | guard issues: none | retried: False_

## Case file
```json
{
  "case_file": {
    "summary": "The user paid Rs 85 lakh to a builder for a flat in 2022 but has not received possession, and is seeking a refund with interest.",
    "in_scope": true,
    "consumer_name": "not provided",
    "opposite_party": "builder",
    "product_or_service": "flat",
    "amount_paid": "Rs 85 lakh",
    "timeline": [
      {
        "date": "2022",
        "event": "Paid Rs 85 lakh for a flat to the builder"
      }
    ],
    "evidence_have": [],
    "evidence_missing": [
      "Payment receipts or bank statements",
      "Builder-buyer agreement or allotment letter",
      "Written correspondence/emails regarding possession timeline"
    ],
    "what_they_want": "Refund with interest",
    "next_steps": [
      "Send a formal legal notice to the builder",
      "Register a complaint with the National Consumer Helpline [KB:NCH]",
      "File a complaint at the State Consumer Disputes Redressal Commission [KB:CPA-JURIS-MONEY] via the e-Jagriti portal [KB:EJAGRITI]"
    ],
    "needs_real_lawyer": true,
    "lawyer_reason": "The amount is above Rs 50 lakh, so the case goes to the State or National Commission; The problem may be more than two years old, so the filing deadline may have passed [KB:CPA-LIMITATION]; The amount paid is Rs 85 lakh (above Rs 50 lakh) [KB:CPA-JURIS-MONEY] and the problem originated in 2022, so the limitation period may be an issue [KB:CPA-LIMITATION]."
  },
  "issues": [],
  "lawyer_flags": [
    "the amount is above Rs 50 lakh, so the case goes to the State or National Commission",
    "the problem may be more than two years old, so the filing deadline may have passed [KB:CPA-LIMITATION]"
  ]
}
```

## Manual review (fill in by hand)
- Verdict (good / partly / bad):
- Notes: