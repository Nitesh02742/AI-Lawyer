# T02_defective_phone_hinglish  (normal)
**Model:** gemini-3.8-flash
**Expected:** Replies in Hinglish; asks about warranty/bill; explains steps.

## Turn 1
**User:** Bhai maine local shop se 18000 ka phone liya tha, 10 din me hi screen me lines aa gayi. Shop wala bol raha hai company ke service center jao, service center bol raha physical damage hai jabki phone kabhi gira hi nahi. Kya karu?

**AI Lawyer:**

Bhai, tension mat lo! Yeh consumer problem hai aur aapka haq banta hai ki ya toh phone thik ho, badla jaye, ya refund mile. Phone bilkul naya hai (10 din purana) aur agar gira nahi hai, toh service center aise hi 'physical damage' bol kar mana nahi kar sakta.

Pehle mujhe kuch baatein batao taaki main aapki sahi madad kar sakoon:

1. Kya aapke paas phone ka **bill (tax invoice)** hai?
2. Kya service center ne aapko koi **job sheet** ya likhit mein statement diya hai jisme unhone 'physical damage' likha hai?
3. Kya phone ke baahar koi dent ya scratch hai, aur kya aapne phone ki condition ki saaf photos/videos li hain?

---

### Aap abhi kya kar sakte hain (Step-by-Step Options):

1. **Saboot ikatha karein (Proof):** 
   - Bill ki copy sambhaal kar rakhein.
   - Phone ke har angle se saaf photos aur video le lein jisme dikhe ki phone par koi dent/crack nahi hai aur screen par lines hain.
   - Service center se written job sheet zaroor lein jahan unhone physical damage ka reason likha ho.

2. **National Consumer Helpline (NCH) par complaint karein:**
   - Aap bina kisi kharche ke National Consumer Helpline par shikayat darj kar sakte hain.
   - Number: **1915** par call karein (8 AM se 8 PM) ya WhatsApp karein **8800001915** par, ya unki website `consumerhelpline.gov.in` par shikayat darj karein [KB:NCH].

3. **Legal Notice aur Consumer Commission:**
   - Agar company ya dukaandaar fir bhi baat nahi sunte, toh aap unhe ek legal notice bhej sakte hain.
   - Phir bhi solution na mile toh aap **District Consumer Commission** mein shikayat darj kar sakte hain. Yeh kaam ab ghar baithe **e-Jagriti** portal par online bhi ho sakta hai [KB:EJAGRITI]. Kyunki phone 18,000 ka hai, yeh District Commission ke under hi aata hai [KB:CPA-JURIS-MONEY].

Aap upar diye gaye 3 sawalon ka jawab dein, fir hum aage ka plan banate hain!

---
*Dhyan rakhein, yeh sirf aam jankari hai, kisi vakeel ki salah nahi.*

_Guard issues: none | retried: False_

## Turn 2
**User:** Bill hai mere paas, aur service center ka job sheet bhi. Mujhe replacement chahiye.

**AI Lawyer:**

Yeh toh bahut achhi baat hai ki aapke paas **bill** aur **job sheet** dono hain! Yeh dono aapke sabse bade saboot hain. Kyunki phone sirf 10 din purana hai aur screen me automatic lines aayi hain, aap replacement paane ke haqdaar hain under Consumer Protection Act, 2019 [KB:CPA-ACT].

Aap replacement lene ke liye step-by-step yeh karein:

### Step 1: Phone Company ke Email / Grievance Officer par mail bhejein
Phone brand ki official website se unke **Grievance Officer** ya **Head of Customer Care** ki email ID nikalein. Unhe ek mail likhein:
- Bill ki photo attach karein.
- Job sheet ki photo attach karein.
- Phone ki saaf photos attach karein (jisse yeh sabit ho sake ki phone par koi dent ya crack nahi hai).
- Likhin ki service center galat bol raha hai ki physical damage hai, jabki phone par koi chot nahi hai. 7 din ke andar phone replacement ki demand karein.

### Step 2: National Consumer Helpline (NCH) par shikayat karein (Bilkul Muft)
Agar mail ka response na aaye ya woh mana kar dein, toh NCH par complaint karein:
- **Call:** 1915 par call karein (subah 8 baje se raat 8 baje tak) [KB:NCH].
- **WhatsApp:** 8800001915 par message karein [KB:NCH].
- **Website:** `consumerhelpline.gov.in` par jaakar complaint register karein [KB:NCH].

### Step 3: Legal Notice bhejein
Agar NCH se bhi baat na bane, toh aap shopkeeper aur phone company dono ko ek **Legal Notice** bhej sakte hain. Legal notice me unhe replacement dene ke liye aakhri mauka diya jata hai. 

### Step 4: District Consumer Commission mein case karein
Agar 15 din me notice ka jawab na mile, toh aap **District Consumer Commission** mein shikayat darj kar sakte hain:
- Aapka case 18,000 ka hai, isliye yeh District Commission ke daayre mein aata hai [KB:CPA-JURIS-MONEY].
- Aap yeh case apne shehar ya jahan se phone kharida tha, wahan ke commission mein file kar sakte hain [KB:CPA-WHERE].
- Aap ghar baithe **e-Jagriti** portal (`ejagriti.gov.in`) par online bhi case file kar sakte hain [KB:EJAGRITI].
- Consumer case file karne ka time problem hone ke **2 saal** ke andar hota hai [KB:CPA-LIMITATION].

---

**Hum aapki kya madad kar sakte hain?**
Aap hamare app mein diye gaye buttons ka use karke apni **Case File** taiyar kar sakte hain aur shopkeeper/company ko bhejne ke liye **Legal Notice** bhi draft karwa sakte hain.

Kya aap pehle company ko mail aur NCH par complaint karna chahenge?

---
*Dhyan rakhein, yeh sirf aam jankari hai, kisi vakeel ki salah nahi.*

_Guard issues: none | retried: False_

## Case file
```json
{
  "case_file": {
    "summary": "The user bought a mobile phone for Rs 18,000 from a local shop. Within 10 days, lines appeared on the screen. The service center is refusing free service by falsely claiming it is physical damage, though the phone was never dropped. The user has the bill and service center job sheet, and wants a replacement.",
    "in_scope": true,
    "consumer_name": "not provided",
    "opposite_party": "Local shop and phone service center / company",
    "product_or_service": "Mobile phone",
    "amount_paid": "Rs 18000",
    "timeline": [
      {
        "date": "10 days ago",
        "event": "Bought a mobile phone from a local shop for Rs 18,000."
      },
      {
        "date": "Within 10 days of purchase",
        "event": "Lines appeared on the phone screen and the service center falsely claimed physical damage."
      }
    ],
    "evidence_have": [
      "Purchase bill",
      "Service center job sheet"
    ],
    "evidence_missing": [
      "Photographs or videos of the phone showing no dents or cracks"
    ],
    "what_they_want": "Replacement of the phone",
    "next_steps": [
      "Send an email to the phone company and grievance officer with the bill and job sheet attached",
      "Register a complaint with the National Consumer Helpline by calling 1915, WhatsApping 8800001915, or visiting consumerhelpline.gov.in [KB:NCH]",
      "Send a legal notice to the shopkeeper and phone company if they do not resolve the issue",
      "File an online complaint on the e-Jagriti portal at ejagriti.gov.in within the 2-year limitation period if needed [KB:EJAGRITI, KB:CPA-LIMITATION]"
    ],
    "needs_real_lawyer": false,
    "lawyer_reason": ""
  },
  "issues": [
    "mentioned the phone number '18000' which is not in the verified sources"
  ]
}
```
## Legal notice
[Your full address]  
[Your phone number]  
[Your email]  
[Date]  

To,  
The Grievance Officer / Management,  
Local shop and phone service center / company  
[Opposite party address - not provided]  

**Subject: Legal notice for replacement of defective mobile phone**

Dear Sir/Madam,

I am writing to bring to your attention a grievance regarding a mobile phone purchased from your establishment. 

On [Date / 10 days ago], I purchased a mobile phone for Rs 18,000 from your local shop. I have the purchase bill as proof of this transaction. 

Within 10 days of purchase, unexpected lines appeared on the phone screen. The phone was never dropped or mishandled in any way. However, when I approached the service center, I was wrongfully refused free service under the false claim of physical damage. I also hold the service center job sheet for this visit. 

As a consumer under the Consumer Protection Act, 2019 [KB:CPA-ACT], I am entitled to receive goods of proper quality without defects. Providing a defective product and refusing valid service is unfair. 

I request you to kindly arrange for a complete replacement of the mobile phone at the earliest. 

Please consider this letter as a final opportunity to resolve this matter within 15 days of receiving this notice. If you fail to respond or resolve this issue within this timeframe, I may be constrained to approach the National Consumer Helpline [KB:NCH] and file a formal complaint before the consumer commission [KB:CPA-ACT].

Sincerely,  

[Your full name - not provided]  

***

*Please note: This is general information and a draft notice based on the details provided, not a formal lawyer's legal advice.*

_Guard issues: none_

## Manual review (fill in by hand)
- Verdict (good / partly / bad):
- Notes: