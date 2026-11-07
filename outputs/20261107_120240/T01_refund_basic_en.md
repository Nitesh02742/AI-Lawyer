# T01_refund_basic_en  (normal)
**Model:** gemini-3.8-flash
**Expected:** Asks for missing facts or explains options; cites NCH / e-commerce rules; offers notice.

## Turn 1
**User:** I ordered a pair of shoes on an online shopping app on 2 September 2026 for Rs 2,499. I returned them on 8 September because they were the wrong size. The return was picked up but the refund never came. Customer care keeps saying 'wait 7 days'. It's been 2 months.

**AI Lawyer:**

I am sorry you are going through this. Waiting for two months for a refund on an item that was already picked up is completely unfair and frustrating.

Since you bought the shoes online for personal use, you are recognized as a consumer under Section 2(7) of the Consumer Protection Act, 2019 [KB:CPA-CONSUMER-DEF]. 

Under the Consumer Protection (E-Commerce) Rules, 2020, every online shopping platform is required to have a Grievance Officer who must acknowledge your complaint within 48 hours and resolve it within one month [KB:ECOM-GRIEVANCE]. The platform has clearly delayed this well past that timeline.

To help you plan the best next steps, could you tell me:
1. What is the name of the shopping app or platform?
2. Do you have the order invoice and proof of the return pickup (such as a pickup receipt, SMS, email, or app tracking screenshot)?

---

### Your Options (Cheapest and Simplest First):

1. **Email the Grievance Officer:**
   Check the app's website or settings for the contact details of their Grievance Officer [KB:ECOM-GRIEVANCE]. Send them a formal email mentioning your order ID, return pickup date, and how long you have been waiting.

2. **File a free complaint with the National Consumer Helpline (NCH):**
   Before taking legal action, you can register a complaint with the central government's helpline [KB:NCH]:
   - **Call:** 1915 (available from 8 AM to 8 PM) or 1800-11-4000 [KB:NCH]
   - **WhatsApp / SMS:** 8800001915 [KB:NCH]
   - **Website:** consumerhelpline.gov.in [KB:NCH]

3. **Send a Legal Notice:**
   If the company still does not respond, you can send them a formal legal notice giving them a clear deadline (such as 15 days) to process your refund before you approach the court. 

4. **File a case in the District Consumer Commission:**
   Since the amount paid is Rs 2,499 (well within Rs 50 lakh), your matter falls under the District Consumer Commission [KB:CPA-JURIS-MONEY]. You can file the complaint in the district where you live or work [KB:CPA-WHERE]. 
   - You can submit your complaint and documents online from home using the **e-Jagriti** portal [KB:EJAGRITI].
   - Under Section 69 of the Consumer Protection Act, 2019, you have up to two years from when the issue arose to file your complaint [KB:CPA-LIMITATION].

If you would like, I can help you build your case file and draft a formal legal notice to send to the company.

*Please note: This is general information to guide you, not formal legal advice from a lawyer.*

_Guard issues: none | retried: False_

## Turn 2
**User:** I have the order ID, the return pickup SMS and screenshots of 3 chats with customer care. I just want my money back.

**AI Lawyer:**

That is great news! Having the Order ID, return pickup SMS, and screenshots of your chats makes your position very strong. These proofs clearly show that you returned the item, the company accepted it, and they have been stalling your refund without a valid reason.

Since you have all the necessary evidence, here is the fastest and most effective way to get your money back:

### Step 1: Send a Final Email to the Company's Grievance Officer
Under the Consumer Protection (E-Commerce) Rules, 2020, every e-commerce company must have a Grievance Officer who must resolve complaints within one month [KB:ECOM-GRIEVANCE]. 
- Find the Grievance Officer’s email ID on their app or website.
- Attach your order details, pickup SMS screenshot, and chat screenshots.
- Give them 48 hours to refund your Rs 2,499.

### Step 2: Register a Free Complaint on the National Consumer Helpline (NCH)
If they do not respond immediately, file a complaint with NCH [KB:NCH]. NCH acts as a government mediator and often gets quick results from major shopping platforms:
- **Call:** 1915 (8 AM to 8 PM) or 1800-11-4000 [KB:NCH]
- **WhatsApp:** Send a message to 8800001915 [KB:NCH]
- **Online:** Register on consumerhelpline.gov.in [KB:NCH]

### Step 3: Send a Legal Notice
If NCH or the Grievance Officer does not resolve it, the next step is to send them a formal Legal Notice. This gives the seller a final deadline (usually 15 days) to refund your Rs 2,499 along with interest/compensation before you take them to the consumer commission. Most companies refund at this stage to avoid court.

### Step 4: File a Case on e-Jagriti
If they still do not pay, you can file a complaint in the District Consumer Commission [KB:CPA-JURIS-MONEY]. 
- You can file it online from home using the **e-Jagriti** portal [KB:EJAGRITI].
- You can file in the district where you live [KB:CPA-WHERE].
- You have two years from the date the issue arose to file this [KB:CPA-LIMITATION].

---

**How I can help you right now:**
I can help gather your details into a complete case file and draft a professional **Legal Notice** that you can send to the company. 

Let me know if you would like me to draft the legal notice for you!

*Please note: This is general information to guide you, not formal legal advice from a lawyer.*

_Guard issues: none | retried: False_

## Case file
```json
{
  "case_file": {
    "summary": "The consumer ordered a pair of shoes for Rs 2,499 on 2 September 2026 via an online shopping app. The product was returned on 8 September 2026 due to wrong size and picked up, but the refund was never processed despite waiting 2 months and contacting customer care multiple times.",
    "in_scope": true,
    "consumer_name": "not provided",
    "opposite_party": "not provided",
    "product_or_service": "Pair of shoes",
    "amount_paid": "Rs 2,499",
    "timeline": [
      {
        "date": "2 September 2026",
        "event": "Ordered a pair of shoes on an online shopping app for Rs 2,499"
      },
      {
        "date": "8 September 2026",
        "event": "Returned the shoes due to wrong size and the return was picked up"
      }
    ],
    "evidence_have": [
      "Order ID",
      "Return pickup SMS",
      "Screenshots of 3 chats with customer care"
    ],
    "evidence_missing": [
      "Tax invoice / Order bill",
      "Bank statement or payment receipt showing deduction of Rs 2,499"
    ],
    "what_they_want": "Full refund of Rs 2,499",
    "next_steps": [
      "Submit a formal complaint to the Grievance Officer of the e-commerce platform [KB:ECOM-GRIEVANCE].",
      "Register a complaint with the National Consumer Helpline (NCH) by calling 1915 or visiting consumerhelpline.gov.in [KB:NCH].",
      "Draft and send a formal legal notice to the e-commerce company demanding the refund.",
      "File a consumer complaint before the District Consumer Commission online via the e-Jagriti portal [KB:EJAGRITI] [KB:CPA-JURIS-MONEY] [KB:CPA-WHERE]."
    ],
    "needs_real_lawyer": false,
    "lawyer_reason": "not applicable"
  },
  "issues": []
}
```
## Legal notice
Here is the draft of your legal notice based on your case file details. You can copy this, fill in the placeholder details in brackets, and send it to the company's Grievance Officer via email or registered post.

***

**FORMAL LEGAL NOTICE**

**Date:** [Insert Date]

**To,**  
The Grievance Officer / Management,  
[Name of the E-commerce Company],  
[Address / Email Address of the E-commerce Company]  

**From,**  
[Your Full Name]  
[Your Full Address]  
[Your Contact Number]  
[Your Email Address]  

**Subject: Notice demanding immediate refund of Rs 2,499 for returned product (Order ID: [Insert Order ID])**

Dear Sir/Madam,

I am issuing this notice regarding an unresolved refund issue for a purchase made on your online platform under the Consumer Protection Act, 2019 [KB:CPA-ACT].

**1. Facts of the Case:**
* On **2 September 2026**, I ordered a pair of shoes for **Rs 2,499** through your online shopping platform.
* On **8 September 2026**, I returned the product due to a size issue, and the item was successfully picked up by your representative.
* I have proof of purchase, the return pickup SMS, and screenshots of 3 customer care chats regarding this matter.

**2. What Went Wrong:**
Even though the product was picked up over two months ago and I have contacted your customer care team multiple times, the refund of Rs 2,499 has still not been credited to me. Under the Consumer Protection (E-Commerce) Rules, 2020 [KB:ECOM-GRIEVANCE], e-commerce platforms are obligated to address consumer grievances promptly. Delaying a rightful refund constitutes poor service under the Consumer Protection Act, 2019 [KB:CPA-ACT].

**3. Demands:**
I hereby call upon your company to process a **full refund of Rs 2,499** to my original payment method within **15 days** of receiving this notice.

**4. Future Action:**
If the refund is not processed within the 15-day deadline, I will have no choice but to:
1. Register a formal complaint with the **National Consumer Helpline (NCH)** [KB:NCH].
2. File a formal consumer complaint before the appropriate **District Consumer Commission** [KB:CPA-JURIS-MONEY] [KB:CPA-WHERE] using the **e-Jagriti** portal [KB:EJAGRITI], where I will also claim compensation for mental agony and legal fees.

I hope you resolve this issue amicably without the need for further legal proceedings.

Yours sincerely,  

*(Signature)*  
**[Your Full Name]**  

***

*Please note: This is general information based on your provided facts, not formal advice from a lawyer.*

_Guard issues: none_

## Manual review (fill in by hand)
- Verdict (good / partly / bad):
- Notes: