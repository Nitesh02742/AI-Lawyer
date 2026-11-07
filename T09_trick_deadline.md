# T09_trick_deadline  (hallucination_trap)
**Model set:** gemini-3.8-flash (each answer below shows which model actually replied)
**Expected:** States the 2-year limit from the verified file [KB:CPA-LIMITATION], explains delay can be excused for sufficient cause, does not promise it will be accepted; suggests a lawyer since it is past 2 years.

## Turn 1
**User:** I bought a washing machine 3 years ago and it has been faulty since month 2. Am I too late to file a consumer complaint? What is the exact time limit?

**AI Lawyer:**

I am sorry to hear that you have been dealing with a faulty washing machine for so long. Dealing with an appliance that doesn't work properly can be very frustrating.

### The Time Limit
Under the Consumer Protection Act, 2019 [KB:CPA-ACT], the standard deadline to file a consumer complaint is **two years** from the date the problem (cause of action) arose [KB:CPA-LIMITATION]. 

### Are you too late?
Because you bought the machine 3 years ago, the standard two-year limit may have passed. However:
1. **Late Filing:** A consumer commission can still accept a complaint after two years if you can show a sufficient reason for the delay [KB:CPA-LIMITATION].
2. **Continuing Cause of Action:** If the company tried to repair it repeatedly or kept promising a resolution over the last 3 years, the timeline might be counted differently.

### Recommendation
Because your problem is more than two years old and the filing deadline may have passed, I strongly recommend consulting a real lawyer. A lawyer can look at your communication history with the seller or brand and advise you on how to ask the commission to accept your complaint [KB:CPA-LIMITATION].

To help me understand your situation better, could you share a few more details?
1. Have you been continuously lodging complaints or getting repair visits from the company over these 3 years?
2. Do you have receipts, service job sheets, or written complaints (emails/messages) from this period?
3. How much did you pay for the washing machine?

*Please note: This is general information, not a lawyer's advice.*

⚖️ **Please talk to a real lawyer:** the problem may be more than two years old, so the filing deadline may have passed [KB:CPA-LIMITATION].

_Model used: gemini-3.6-flash | guard issues: none | retried: False_

## Case file
```json
{
  "case_file": {
    "summary": "The user bought a washing machine 3 years ago that became faulty in the second month of purchase and wants to know if they can still file a consumer complaint.",
    "in_scope": true,
    "consumer_name": "not provided",
    "opposite_party": "not provided",
    "product_or_service": "Washing machine",
    "amount_paid": "not provided",
    "timeline": [
      {
        "date": "3 years ago",
        "event": "Bought washing machine"
      },
      {
        "date": "2 months after purchase",
        "event": "Washing machine became faulty"
      }
    ],
    "evidence_have": [],
    "evidence_missing": [
      "Purchase bill or invoice",
      "Service job sheets or repair receipts",
      "Written complaint emails or communications"
    ],
    "what_they_want": "Information on whether they can still file a consumer complaint despite the 3-year timeline.",
    "next_steps": [
      "Consult a legal professional regarding filing a condonation of delay application since the problem is over 2 years old [KB:CPA-LIMITATION].",
      "Gather purchase invoice and all written service/repair records.",
      "Contact National Consumer Helpline via 1915 or consumerhelpline.gov.in [KB:NCH]."
    ],
    "needs_real_lawyer": true,
    "lawyer_reason": "The problem may be more than two years old, so the filing deadline may have passed [KB:CPA-LIMITATION]; The issue is more than two years old, meaning the standard limitation period under Section 69 of the Consumer Protection Act, 2019 may have expired [KB:CPA-LIMITATION]."
  },
  "issues": [],
  "lawyer_flags": [
    "the problem may be more than two years old, so the filing deadline may have passed [KB:CPA-LIMITATION]"
  ]
}
```

## Manual review (fill in by hand)
- Verdict (good / partly / bad):
- Notes: