# T01_refund_basic_en  (normal)
**Model set:** gemini-3.8-flash (each answer below shows which model actually replied)
**Expected:** Asks for missing facts or explains options; cites NCH / e-commerce rules; offers notice.

## Turn 1
**User:** I ordered a pair of shoes on an online shopping app on 2 September 2026 for Rs 2,499. I returned them on 8 September because they were the wrong size. The return was picked up but the refund never came. Customer care keeps saying 'wait 7 days'. It's been 2 months.

**AI Lawyer:**

I understand how frustrating it is to wait two months for your hard-earned money, especially after the product was already picked up. You may have a claim here as a consumer who paid for goods online [KB:CPA-CONSUMER-DEF].

To help you better, could you answer a quick question?
1. What is the name of the online shopping app?
2. Do you have proof of the purchase and the pickup receipt or return tracking status?

---

Here are the step-by-step options available to you, starting with the simplest and free methods:

### Step 1: Write to the Grievance Officer
Under online shopping rules, every e-commerce platform must display the contact details of a Grievance Officer [KB:ECOM-GRIEVANCE]. 
- Find their email address in the app's "Contact Us", "Help", or "Terms of Use" section.
- Send a detailed email with your order ID, date of pickup, payment proof, and photos of customer care chat logs.
- By law, the officer must acknowledge your complaint within 48 hours and resolve it within one month [KB:ECOM-GRIEVANCE].

### Step 2: Register a complaint with the National Consumer Helpline (NCH)
If the company still does not respond or refund your money, you can lodge a free complaint with the National Consumer Helpline [KB:NCH]:
- **Call:** 1915 (8 AM to 8 PM) or 1800-11-4000 [KB:NCH]
- **WhatsApp:** Send a message to 8800001915 [KB:NCH]
- **Online:** Visit consumerhelpline.gov.in or use the NCH or UMANG app [KB:NCH]

### Step 3: Send a Legal Notice
If NCH does not solve the issue, you can send a formal legal notice to the company giving them a deadline to refund your money.

### Step 4: File a Consumer Case Online
Since the amount paid is Rs 2,499 (which is under Rs 50 lakh), your case falls under the District Consumer Commission [KB:CPA-JURIS-MONEY]. You can file a case online from home using the **e-Jagriti** portal [KB:EJAGRITI]. 

---

If you'd like, I can help you compile your details to build a strong case file or draft a formal notice to send to the company.

*This is general information, not a lawyer's advice.*

_Model used: gemini-3.6-flash | guard issues: none | retried: False_

## Turn 2
**User:** I have the order ID, the return pickup SMS and screenshots of 3 chats with customer care. I just want my money back.

**AI Lawyer:**

That is great! Having the order ID, the return pickup SMS, and the chat screenshots gives you solid proof to support your claim. 

Since you paid Rs 2,499 (which is well within the limit of up to Rs 50 lakh), your matter comes under the District Commission [KB:CPA-JURIS-MONEY]. You also have plenty of time, as consumer complaints can be filed within two years from when the issue started [KB:CPA-LIMITATION].

Here is what you should do next to get your refund:

### 1. Email the Grievance Officer
Send a firm email to the app’s Grievance Officer attaching all your screenshots, the return pickup SMS, and the order ID. By law, the Grievance Officer must acknowledge your email within 48 hours and resolve the issue within one month [KB:ECOM-GRIEVANCE].

### 2. Report to the National Consumer Helpline (NCH)
If they still ignore you, lodge a free complaint with the National Consumer Helpline:
- **Call:** 1915 (8 AM to 8 PM) or 1800-11-4000 [KB:NCH]
- **WhatsApp:** Send your complaint to 8800001915 [KB:NCH]
- **Website/App:** Log in to consumerhelpline.gov.in or use the NCH or UMANG app [KB:NCH]

### 3. Send a Legal Notice or File on e-Jagriti
If NCH does not resolve it, you can send the company a formal legal notice giving them a short deadline to pay. If they still fail to refund, you can file a case online from home through the **e-Jagriti** portal [KB:EJAGRITI].

---

If you want, I can help you compile your documents into a organized case file or draft a formal legal notice to send to the company.

*This is general information, not a lawyer's advice.*

_Model used: gemini-3.6-flash | guard issues: none | retried: False_

## Case file
```json
{
  "case_file": {
    "summary": "Consumer purchased shoes online for Rs 2,499, returned them due to incorrect size, and the return was picked up, but the refund has not been processed for two months despite follow-ups with customer care.",
    "in_scope": true,
    "consumer_name": "not provided",
    "opposite_party": "not provided",
    "product_or_service": "Pair of shoes",
    "amount_paid": "Rs 2,499",
    "timeline": [
      {
        "date": "2 September 2026",
        "event": "Ordered a pair of shoes for Rs 2,499 on an online shopping app."
      },
      {
        "date": "8 September 2026",
        "event": "Returned the shoes due to wrong size."
      },
      {
        "date": "2 months after purchase",
        "event": "Return picked up but refund not received after repeatedly contacting customer care."
      }
    ],
    "evidence_have": [
      "Order ID",
      "Return pickup SMS",
      "Screenshots of 3 chats with customer care"
    ],
    "evidence_missing": [
      "Bank statement or payment receipt showing payment of Rs 2,499",
      "Name and email address of the online shopping app / Grievance Officer"
    ],
    "what_they_want": "Full refund of Rs 2,499",
    "next_steps": [
      "Send an email with order details and proof to the seller's Grievance Officer [KB:ECOM-GRIEVANCE].",
      "Register a free complaint with the National Consumer Helpline by calling 1915 or visiting consumerhelpline.gov.in [KB:NCH].",
      "Draft and send a formal legal notice to the company.",
      "File a consumer complaint online against the company through the e-Jagriti portal [KB:EJAGRITI]."
    ],
    "needs_real_lawyer": false,
    "lawyer_reason": ""
  },
  "issues": [],
  "lawyer_flags": []
}
```
## Legal notice
**LEGAL NOTICE**

**Date:** [Date of sending notice]

**To:**  
The Grievance Officer / Management  
[Name of the Online Shopping Company]  
[Company Address]  

**From:**  
[Your Full Name]  
[Your Full Address]  

**Subject:** Legal Notice for pending refund of Rs 2,499 regarding Order ID: [Your Order ID]

Dear Sir/Madam,

I am writing this notice regarding an unfulfilled refund for a purchase made on your online platform.

**Facts of the Matter:**
1. On **2 September 2026**, I ordered a pair of shoes for **Rs 2,499** through your online shopping platform.
2. On **8 September 2026**, I initiated a return for the shoes due to an incorrect size.
3. The return item was successfully picked up by your logistics team. However, even after two months from the purchase date and multiple follow-ups with your customer care team, the refund of Rs 2,499 has not been processed.
4. I have retained all relevant records, including the Order ID, return pickup SMS, and screenshots of customer care conversations.

Under the Consumer Protection (E-Commerce) Rules, 2020 [KB:ECOM-GRIEVANCE], an e-commerce platform is required to have a Grievance Officer who must acknowledge complaints within 48 hours and resolve them within one month of receipt.

**My Demand:**
I request you to kindly process the full refund of **Rs 2,499** to my account within **15 days** of receiving this notice.

**Further Action:**
If the refund is not processed within 15 days, I may proceed to register a complaint with the National Consumer Helpline [KB:NCH] (by calling 1915 or visiting consumerhelpline.gov.in [KB:NCH]) and file a formal consumer complaint before the appropriate District Consumer Commission [KB:CPA-ACT] online through the e-Jagriti portal [KB:EJAGRITI].

Sincerely,

[Your Full Name]  
[Your Mobile Number]  

---
*This is general information, not a lawyer's advice.*

_Guard issues: none_

## Manual review (fill in by hand)
- Verdict (good / partly / bad):
- Notes: