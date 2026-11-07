# T04_messy_story  (messy)
**Model set:** gemini-3.8-flash (each answer below shows which model actually replied)
**Expected:** Untangles the timeline; asks focused questions; does not invent dates.

## Turn 1
**User:** ok so basically gym took 12 months fees like 15k in jan or maybe feb, then they shut the branch in june?? said go to other branch which is 14 km away, i asked for refund for remaining months they said no refund policy. also trainer was rude earlier but whatever. my friend also same issue. what can we do

**AI Lawyer:**

I am really sorry to hear about this. Paying for a full year upfront and having the gym close its branch just a few months later is very frustrating, especially when the alternative branch is 14 km away.

Since you paid for a service, you count as a consumer [KB:CPA-CONSUMER-DEF] under the Consumer Protection Act, 2019 [KB:CPA-ACT]. Even if they mention a "no refund policy," you may have a claim to get a refund for the unused months.

To help you better, could you tell me:
1. Do you have payment receipts or bank screenshots showing the ₹15,000 paid?
2. Do you have any written proof (like WhatsApp messages, emails, or notices) showing that the branch closed and that they refused your refund?

---

### What you can do (Step-by-Step)

Here are your options, starting from the easiest and cheapest:

1. **National Consumer Helpline (NCH)**  
   Before taking legal steps, you can file a free complaint with the National Consumer Helpline. You can call **1915** (8 AM to 8 PM) or **1800-11-4000**, send a WhatsApp message to **8800001915**, or submit it online at **consumerhelpline.gov.in** [KB:NCH].

2. **Legal Notice**  
   You can send a formal legal notice to the gym owner asking for a pro-rata refund for the remaining months. This often pushes businesses to resolve the matter.

3. **District Consumer Commission**  
   If they still refuse, you can file a complaint at the District Consumer Commission [KB:CPA-WHERE] because the payment amount is under Rs 50 lakh [KB:CPA-JURIS-MONEY]. You can file this online through the **e-Jagriti** portal [KB:EJAGRITI]. Please note that consumer complaints must be filed within 2 years from when the issue arose [KB:CPA-LIMITATION].

If you like, I can help you build your case file and draft a legal notice to send to the gym management.

*This is general consumer information, not a lawyer's legal advice.*

_Model used: gemini-3.6-flash | guard issues: none | retried: False_

## Case file
```json
{
  "case_file": {
    "summary": "The consumer paid Rs 15,000 for a 12-month gym membership in January or February. The gym closed the branch in June and asked the consumer to go to another branch 14 km away. The consumer requested a refund for the remaining months, but the gym refused citing a no-refund policy.",
    "in_scope": true,
    "consumer_name": "not provided",
    "opposite_party": "not provided",
    "product_or_service": "Gym membership",
    "amount_paid": "Rs 15,000",
    "timeline": [
      {
        "date": "January or February",
        "event": "Paid Rs 15,000 for 12 months gym membership"
      },
      {
        "date": "June",
        "event": "Gym shut down the branch, asked consumer to go to another branch 14 km away, and refused refund request for remaining months"
      }
    ],
    "evidence_have": [],
    "evidence_missing": [
      "Payment receipts or bank statements showing Rs 15,000 paid",
      "Written notice or message regarding branch closure",
      "Written refusal of refund from gym management"
    ],
    "what_they_want": "Refund for remaining months",
    "next_steps": [
      "File a complaint free with National Consumer Helpline by calling 1915 or online at consumerhelpline.gov.in [KB:NCH]",
      "Send a formal legal notice to the gym owner demanding a pro-rata refund for remaining months",
      "File a complaint at the District Consumer Commission [KB:CPA-WHERE] online using the e-Jagriti portal [KB:EJAGRITI]"
    ],
    "needs_real_lawyer": false,
    "lawyer_reason": ""
  },
  "issues": [],
  "lawyer_flags": []
}
```
## Legal notice
Date: [Date]

To,  
The Manager / Grievance Officer,  
[Name of Gym / Opposite Party],  
[Address of Gym / Opposite Party]  

**Subject: Notice demanding refund of unused gym membership fee**

Dear Sir/Madam,

I am writing to bring to your notice a dispute regarding my gym membership under the Consumer Protection Act, 2019 [KB:CPA-ACT], as a consumer who paid for your services [KB:CPA-CONSUMER-DEF].

The facts of the matter are as follows:
1. In January or February, I paid an amount of Rs 15,000 for a 12-month gym membership at your branch.
2. In June, your company shut down this branch and asked me to attend another branch situated 14 km away.
3. As traveling to the new location is not practical for me, I requested a pro-rata refund for the remaining months of my membership. However, your management refused to process the refund, citing a no-refund policy.

Since the service at the agreed branch has been discontinued, I request you to issue a refund for the remaining unused months of my membership within 15 days of receiving this notice.

If I do not receive a resolution or response within 15 days, I may register a complaint with the National Consumer Helpline by calling 1915 or online at consumerhelpline.gov.in [KB:NCH]. I may also proceed to file a formal complaint before the District Consumer Commission [KB:CPA-WHERE] online via the e-Jagriti portal [KB:EJAGRITI].

I hope to resolve this matter amicably. 

Yours sincerely,

[Your Full Name]  
[Your Address]  
[Your Contact Info]  

***
*This is general information, not a lawyer's advice.*

_Guard issues: none_

## Manual review (fill in by hand)
- Verdict (good / partly / bad):
- Notes: