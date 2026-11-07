# T02_defective_phone_hinglish  (normal)
**Model set:** gemini-3.8-flash (each answer below shows which model actually replied)
**Expected:** Replies in Hinglish; asks about warranty/bill; explains steps.

## Turn 1
**User:** Bhai maine local shop se 18000 ka phone liya tha, 10 din me hi screen me lines aa gayi. Shop wala bol raha hai company ke service center jao, service center bol raha physical damage hai jabki phone kabhi gira hi nahi. Kya karu?

**AI Lawyer:**

Aap pareshan mat hoiye, main aapki poori madad karunga. Phone sirf 10 din purana hai, toh aapke paas iska solution paane ka claim ho sakta hai.

Sahi raasta batane ke liye, mujhe bass **3 choti baatein** bataiye:
1. Kya aapke paas phone ka pakka bill (invoice) hai?
2. Kya service center ne aapko koi job sheet ya written paper diya hai jisme unhone 'physical damage' likha hai?
3. Aap abhi kya chahte hain — phone replacement, free repair, ya refund?

---

**Aap abhi ye steps le sakte hain:**

1. **Brand ke Grievance Officer ko Mail karein:** Phone brand ki official website par jaakar unke Grievance Officer ya Customer Head ko mail bhejein. Mail me bill aur job sheet ki photo lagayein aur likhein ki phone gira nahi hai.
2. **National Consumer Helpline (NCH):** Agar shopkeeper ya service center sunvai nahi karta, toh aap free me National Consumer Helpline par complaint darj kara sakte hain [KB:NCH]. 
   * **Call:** 1915 par call karein [KB:NCH]
   * **WhatsApp:** 8800001915 par message karein [KB:NCH]

Aap upar diye gaye sawalon ka jawab dein, fir agar zaroorat hui toh hum aapka case file taiyaar karne aur legal notice bhejne me bhi madad kar sakte hain.

*Yeh sirf aam jankari hai, kisi vakeel ki salah nahi hai.*

_Model used: gemini-3.6-flash | guard issues: none | retried: False_

## Turn 2
**User:** Bill hai mere paas, aur service center ka job sheet bhi. Mujhe replacement chahiye.

**AI Lawyer:**

Aapke paas Bill aur Job Sheet dono hain, yeh bahut acchi baat hai. Isse aapka case majboot hota hai. 

Chunki aapne 18,000 me phone khareeda hai aur bill aapke paas hai, aap Consumer Protection Act, 2019 ke tehat ek consumer hain [KB:CPA-CONSUMER-DEF]. 

Aap replacement ke liye ye stepwise raaste apna sakte hain:

1. **Brand ke Head / Grievance Officer ko Mail karein:** 
   Phone company ki website se unke Grievance Officer ki email ID lein. Mail me Bill aur Job sheet ki photo attach karein. Likhein ki phone bilkul gira nahi hai aur 10 din ke andar screen me lines aayi hain. Unse replacement ki maang karein.

2. **National Consumer Helpline (NCH) me complaint karein:**
   Agar company ya shopkeeper aapki baat nahi sunte, toh aap free me National Consumer Helpline par complaint register kara sakte hain [KB:NCH]:
   * **Call:** 1915 (subah 8 baje se raat 8 baje tak) [KB:NCH]
   * **WhatsApp:** 8800001915 [KB:NCH]
   * **Website:** consumerhelpline.gov.in [KB:NCH]

3. **Legal Notice aur Consumer Commission:**
   Agar NCH se bhi hal nahi nikalta, toh aap unhe ek formal Legal Notice bhej sakte hain. Uske baad bhi hal na mile toh aap apne jile ki District Consumer Commission me case file kar sakte hain [KB:CPA-JURIS-MONEY] [KB:CPA-WHERE]. Iski complaint aap ghar baithe online portal **e-Jagriti** par bhi daakhil kar sakte hain [KB:EJAGRITI].

Agar aap chahein, toh main aapka case file taiyaar karne aur unhe bhejne ke liye Legal Notice draft karne me aapki madad kar sakta hoon (aap app me diye gaye buttons par click kar sakte hain).

*Yeh sirf aam jankari hai, kisi vakeel ki salah nahi hai.*

_Model used: gemini-3.6-flash | guard issues: none | retried: False_

## Case file
```json
{
  "case_file": {
    "summary": "User purchased a phone for Rs 18,000 from a local shop. Within 10 days, lines appeared on the screen. The shopkeeper referred the user to the brand service center, where the service center claimed physical damage in the job sheet, which the user denies as the phone was never dropped.",
    "in_scope": true,
    "consumer_name": "not provided",
    "opposite_party": "Local shop and brand service center",
    "product_or_service": "Phone",
    "amount_paid": "Rs 18,000",
    "timeline": [
      {
        "date": "not provided",
        "event": "User purchased phone for Rs 18,000 from local shop."
      },
      {
        "date": "10 days after purchase",
        "event": "Lines appeared on the screen."
      },
      {
        "date": "not provided",
        "event": "Shopkeeper instructed user to visit brand service center."
      },
      {
        "date": "not provided",
        "event": "Service center inspected phone and issued job sheet citing physical damage."
      }
    ],
    "evidence_have": [
      "Purchase bill",
      "Service center job sheet"
    ],
    "evidence_missing": [
      "Photos of screen showing lines without external physical damage",
      "Email correspondence with seller or brand grievance officer"
    ],
    "what_they_want": "Phone replacement",
    "next_steps": [
      "Email the brand's Grievance Officer with copies of the bill and job sheet requesting replacement.",
      "Register a free complaint with the National Consumer Helpline via call at 1915 or WhatsApp at 8800001915 [KB:NCH].",
      "Issue a legal notice to the seller and service center.",
      "File a complaint at the District Consumer Commission [KB:CPA-JURIS-MONEY] via the e-Jagriti portal [KB:EJAGRITI]."
    ],
    "needs_real_lawyer": false,
    "lawyer_reason": "none"
  },
  "issues": [],
  "lawyer_flags": []
}
```
## Legal notice
**LEGAL NOTICE**

**From:**  
[Your Full Name]  
[Your Full Address]  

**To:**  
[Name of Local Shop / Brand Service Center / Grievance Officer]  
[Address of Shop / Service Center]  

**Date:** [Date of sending notice]  

**Subject: Notice requesting replacement for defective phone (Payment of Rs 18,000)**

Sir/Madam,

I am writing this notice regarding a phone I purchased from your shop/brand for an amount of Rs 18,000 on [Date of Purchase]. As I have paid for this product for personal use, I am a consumer under Section 2(7) of the Consumer Protection Act, 2019 [KB:CPA-CONSUMER-DEF].

The relevant facts of the case are as follows:
1. On [Date of Purchase], I purchased the phone for Rs 18,000 from [Name of Shop] (Purchase Bill is in my possession).
2. Within 10 days of purchase, vertical/horizontal lines appeared on the screen of the phone.
3. As instructed by the shopkeeper, I visited the brand service center to report the defect.
4. The service center inspected the phone and issued a job sheet stating that the defect is due to physical damage. 
5. I deny the finding in the job sheet, as the phone was never dropped, misused, or physically damaged.

Because the product developed display lines within 10 days of purchase without any physical drop, I hereby request you to provide a **complete replacement of the phone** with a new, defect-free unit.

Please resolve this matter and arrange for the replacement within **15 days** from the receipt of this notice. 

If this issue is not resolved within 15 days, I may register a complaint with the National Consumer Helpline by calling 1915 or sending a WhatsApp message to 8800001915 [KB:NCH]. Furthermore, I may initiate appropriate proceedings against you before the District Consumer Commission [KB:CPA-JURIS-MONEY] online via the e-Jagriti portal [KB:EJAGRITI] under the Consumer Protection Act, 2019 [KB:CPA-ACT].

Yours sincerely,

[Your Name]  
[Your Contact Details]  

***

*This is general information, not a lawyer's advice.*

_Guard issues: none_

## Manual review (fill in by hand)
- Verdict (good / partly / bad):
- Notes: