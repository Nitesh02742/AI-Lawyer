"""AI Lawyer: Streamlit chat app. Run with:  streamlit run app.py"""

import json
import os
from datetime import datetime

import streamlit as st

from lawyer_core import MODEL_NAME, Lawyer

st.set_page_config(page_title="AI Lawyer", page_icon="⚖️", layout="centered")


# ---------------------------------------------------------------- setup
def get_api_key():
    try:
        return st.secrets["GEMINI_API_KEY"]
    except Exception:
        return os.environ.get("GEMINI_API_KEY", "")


@st.cache_resource
def get_lawyer(key, model):
    return Lawyer(api_key=key, model_name=model)


api_key = get_api_key()
with st.sidebar:
    st.header("⚖️ AI Lawyer")
    st.caption("Help with consumer problems in India: refunds, defective products, bad service, online shopping.")
    if not api_key:
        api_key = st.text_input("Gemini API key", type="password")
    model = st.text_input("Model", value=MODEL_NAME, help="Swap to any Gemini model name")
    st.divider()
    st.markdown(
        "**What I can't help with:** criminal cases, property or rent, family matters, salary disputes, "
        "cyber fraud. For these, please see a lawyer or your District Legal Services Authority."
    )

if not api_key:
    st.info("Add your Gemini API key in the sidebar to start.")
    st.stop()

lawyer = get_lawyer(api_key, model)

if "history" not in st.session_state:
    st.session_state.history = []      # what the model sees
    st.session_state.log = []          # everything, for download / raw outputs
    st.session_state.case_file = None
    st.session_state.notice = None
    st.session_state.mic_key = 0

st.title("⚖️ AI Lawyer")
st.caption(
    "Tell me your problem in Hindi, English or your language, by typing or by voice. "
    "I give general information, not a lawyer's advice."
)


def show_answer(result):
    st.markdown(result["text"])
    if result.get("model_used"):
        st.caption(f"Answered by {result['model_used']}")
    if result.get("sources"):
        with st.expander("📚 Sources (verified)"):
            for s in result["sources"]:
                st.markdown(f"- **{s['title']}**: {s['url']}")
    if result.get("issues"):
        st.warning(
            "⚠️ This answer may mention things I could not verify: "
            + "; ".join(result["issues"])
            + ". Please double-check with a lawyer or the National Consumer Helpline."
        )


# ---------------------------------------------------------------- chat history
if not st.session_state.history:
    with st.chat_message("assistant"):
        st.markdown(
            "Namaste 🙏 What happened? For example: *\"I ordered a phone, it came broken and the seller "
            "is not giving a refund.\"* / *\"मेरा रिफंड 2 महीने से नहीं आया।\"*"
        )

for entry in st.session_state.log:
    if entry["type"] == "user":
        with st.chat_message("user"):
            st.markdown(("🎤 " if entry.get("voice") else "") + entry["text"])
    elif entry["type"] == "assistant":
        with st.chat_message("assistant"):
            show_answer(entry)


# ---------------------------------------------------------------- input
def handle_user_text(text, voice=False):
    st.session_state.history.append({"role": "user", "text": text})
    st.session_state.log.append({"type": "user", "text": text, "voice": voice, "time": datetime.now().isoformat()})
    with st.spinner("Thinking..."):
        try:
            result = lawyer.reply(st.session_state.history)
        except Exception as e:
            st.error(f"The AI service failed: {e}. Please try again in a minute.")
            st.session_state.history.pop()
            st.session_state.log.pop()
            return
    st.session_state.history.append({"role": "assistant", "text": result["text"]})
    st.session_state.log.append({"type": "assistant", **result, "time": datetime.now().isoformat()})
    st.rerun()


audio = st.audio_input("🎤 Speak your problem", key=f"mic_{st.session_state.mic_key}")
if audio is not None:
    with st.spinner("Listening..."):
        try:
            transcript = lawyer.transcribe(audio.getvalue(), mime=audio.type or "audio/wav")
        except Exception as e:
            transcript = ""
            st.error(f"Could not understand the voice note: {e}")
    st.session_state.mic_key += 1
    if transcript:
        handle_user_text(transcript, voice=True)

prompt = st.chat_input("Type your problem...")
if prompt:
    handle_user_text(prompt)


# ---------------------------------------------------------------- tools
st.divider()
col1, col2, col3 = st.columns(3)
has_chat = len(st.session_state.history) >= 2

if col1.button("📁 Build my case file", disabled=not has_chat, use_container_width=True):
    with st.spinner("Organising your case..."):
        st.session_state.case_file = lawyer.case_file(st.session_state.history)
    st.session_state.log.append({"type": "case_file", **st.session_state.case_file})

if col2.button("📝 Draft legal notice", disabled=st.session_state.case_file is None, use_container_width=True):
    with st.spinner("Drafting your notice..."):
        st.session_state.notice = lawyer.legal_notice(st.session_state.case_file["case_file"])
    st.session_state.log.append({"type": "legal_notice", **st.session_state.notice})

col3.download_button(
    "💾 Save conversation",
    data=json.dumps(st.session_state.log, indent=2, ensure_ascii=False),
    file_name=f"ai_lawyer_{datetime.now():%Y%m%d_%H%M}.json",
    disabled=not st.session_state.log,
    use_container_width=True,
)

cf = st.session_state.case_file
if cf:
    st.subheader("📁 Your case file")
    c = cf["case_file"]
    if "error" in c:
        st.error("Could not build the case file. Please add more details and try again.")
    else:
        if not c.get("in_scope", True) or c.get("needs_real_lawyer"):
            st.error(f"👩‍⚖️ Please consult a real lawyer. {c.get('lawyer_reason', '')}")
        st.markdown(f"**Summary:** {c.get('summary', '')}")
        st.markdown(
            f"**Against:** {c.get('opposite_party', 'not provided')} · "
            f"**Product/service:** {c.get('product_or_service', 'not provided')} · "
            f"**Paid:** {c.get('amount_paid', 'not provided')}"
        )
        if c.get("timeline"):
            st.markdown("**Timeline**")
            st.table([{"When": t["date"], "What happened": t["event"]} for t in c["timeline"]])
        a, b = st.columns(2)
        a.markdown("**✅ Proof you have**\n" + "\n".join(f"- {x}" for x in c.get("evidence_have", [])) or "-")
        b.markdown("**❗ Proof to collect**\n" + "\n".join(f"- {x}" for x in c.get("evidence_missing", [])) or "-")
        st.markdown("**Next steps**\n" + "\n".join(f"{i+1}. {s}" for i, s in enumerate(c.get("next_steps", []))))
    if cf.get("issues"):
        st.warning("⚠️ Unverified references found: " + "; ".join(cf["issues"]))

nt = st.session_state.notice
if nt:
    st.subheader("📝 Draft legal notice")
    st.caption("Fill in the [placeholders], read it carefully, and send it by email and registered post.")
    show_answer(nt)
    st.download_button("⬇️ Download notice (.txt)", nt["text"], file_name="legal_notice.txt")
