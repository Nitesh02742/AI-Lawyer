# T03_hindi_flight_refund  (normal)
**Model set:** gemini-3.8-flash (each answer below shows which model actually replied)
**Expected:** Replies in Hindi (Devanagari); asks details; no invented aviation rules.

## Turn 1
**User:** मेरी फ्लाइट एयरलाइन ने कैंसिल कर दी थी, 6200 रुपये का टिकट था। एक महीना हो गया, रिफंड नहीं आया। मैंने ट्रैवल वेबसाइट से टिकट बुक किया था।

**AI Lawyer:**

नमस्ते! आपकी परेशानी समझ आ रही है। फ्लाइट कैंसिल होने के बाद एक महीने तक रिफंड न मिलना वाकई तनावपूर्ण हो सकता है। चूंकि आपने सेवा के लिए पैसे दिए हैं, इसलिए उपभोक्ता कानून के तहत आप एक उपभोक्ता (कंज्यूमर) हैं [KB:CPA-CONSUMER-DEF]।

आपकी स्थिति को बेहतर समझने के लिए कृपया मुझे ये बातें बताएं:
1. क्या आपने ट्रैवल वेबसाइट या एयरलाइन के ग्रीवांस ऑफिसर (Grievance Officer) से लिखित में शिकायत की है?
2. क्या आपके पास टिकट, पेमेंट की रसीद और एयरलाइन द्वारा फ्लाइट कैंसिलेशन का मैसेज या ईमेल मौजूद है?
3. क्या वेबसाइट या एयरलाइन ने रिफंड न देने का कोई कारण बताया है?

आप इस मामले में सबसे सस्ते और आसान तरीके से शुरुआत कर सकते हैं:

1. **कंपनी के ग्रीवांस ऑफिसर से संपर्क करें:** नियम के मुताबिक हर ई-कॉमर्स और ऑनलाइन ट्रैवल प्लेटफॉर्म पर एक ग्रीवांस ऑफिसर का होना जरूरी है [KB:ECOM-GRIEVANCE]। उन्हें अपनी शिकायत और सबूत ईमेल करें।
2. **नेशनल कंज्यूमर हेल्पलाइन (NCH) पर शिकायत दर्ज करें:** अगर ग्रीवांस ऑफिसर से बात न बने, तो आप नेशनल कंज्यूमर हेल्पलाइन पर बिना किसी कोर्ट फीस के शिकायत कर सकते हैं [KB:NCH]।
   - कॉल करें: 1915 (सुबह 8 बजे से रात 8 बजे तक) या 1800-11-4000 [KB:NCH]
   - व्हाट्सएप / SMS करें: 8800001915 [KB:NCH]
   - वेबसाइट: consumerhelpline.gov.in पर दर्ज करें [KB:NCH]
3. **लीगल नोटिस और कंज्यूमर कमीशन:** इसके बाद भी रिफंड न मिलने पर आप लीगल नोटिस भेज सकते हैं। 50 लाख रुपये तक के मामलों के लिए आप ई-जागृति (e-Jagriti) पोर्टल के जरिए ऑनलाइन जिला उपभोक्ता आयोग (District Commission) में शिकायत दर्ज कर सकते हैं [KB:CPA-JURIS-MONEY], [KB:EJAGRITI]।

अगर आप चाहें, तो मैं आपकी केस फाइल तैयार करने और लीगल नोटिस का ड्राफ्ट बनाने में आपकी मदद कर सकता हूं।

यह केवल सामान्य जानकारी है, किसी वकील की कानूनी सलाह नहीं है।

_Model used: gemini-3.6-flash | guard issues: none | retried: False_

## Case file
```json
{
  "case_file": {
    "summary": "The user booked a flight ticket for Rs 6,200 through a travel website. The airline cancelled the flight. One month has passed, but the refund has not been received.",
    "in_scope": true,
    "consumer_name": "not provided",
    "opposite_party": "Travel website / Airline (exact names not provided)",
    "product_or_service": "Flight ticket booking service",
    "amount_paid": "Rs 6,200",
    "timeline": [
      {
        "date": "1 month ago",
        "event": "Flight was cancelled by the airline and refund of Rs 6,200 was not provided"
      }
    ],
    "evidence_have": [],
    "evidence_missing": [
      "Flight ticket / booking confirmation",
      "Payment receipt / transaction proof",
      "Flight cancellation message or email from the airline",
      "Communications / emails sent to travel website or airline"
    ],
    "what_they_want": "Refund of Rs 6,200",
    "next_steps": [
      "Contact the grievance officer of the travel website and airline [KB:ECOM-GRIEVANCE].",
      "Lodge a complaint with the National Consumer Helpline (NCH) by calling 1915 or 1800-11-4000, or via WhatsApp at 8800001915 or online at consumerhelpline.gov.in [KB:NCH].",
      "Send a legal notice to the travel website and airline.",
      "File a consumer complaint online via the e-Jagriti portal before the District Consumer Commission [KB:CPA-JURIS-MONEY] [KB:EJAGRITI]."
    ],
    "needs_real_lawyer": false,
    "lawyer_reason": ""
  },
  "issues": [],
  "lawyer_flags": []
}
```

## Manual review (fill in by hand)
- Verdict (good / partly / bad):
- Notes: