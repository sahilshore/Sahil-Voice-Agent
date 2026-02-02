from dotenv import load_dotenv
load_dotenv()

import os
import streamlit as st
import tempfile
from openai import OpenAI

from ai_agent import get_ai_response

# ---------------- OPENAI CLIENT ----------------
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="Sahil Voice Agent", page_icon="🎤")
st.title("🎤 Sahil – Voice Agent")

st.caption("Speak directly or switch to chat mode.")

# ---------------- MODE TOGGLE ----------------
mode = st.toggle("💬 Switch to Chat Mode", value=False)

# ---------------- SESSION STATE ----------------
if "history" not in st.session_state:
    st.session_state.history = []

if "last_input" not in st.session_state:
    st.session_state.last_input = ""

# =====================================================
# 🎤 VOICE MODE
# =====================================================
if not mode:
    audio = st.audio_input("Speak to the agent")

    if audio is not None:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
            f.write(audio.getbuffer())
            audio_path = f.name

        transcription = client.audio.transcriptions.create(
            model="whisper-1",
            file=open(audio_path, "rb"),
            language="en"
        )

        user_text = transcription.text.strip()

        if user_text and user_text != st.session_state.last_input:
            st.session_state.last_input = user_text

            ai_text = get_ai_response(user_text)

            st.session_state.history.append(("You", user_text))
            st.session_state.history.append(("AI", ai_text))

            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
                speech_path = f.name

            with client.audio.speech.with_streaming_response.create(
                model="gpt-4o-mini-tts",
                voice="alloy",
                input=ai_text,
            ) as response:
                response.stream_to_file(speech_path)

            st.markdown("**🔊 Sahil’s Response**")
            st.audio(speech_path)

# =====================================================
# 💬 CHAT MODE
# =====================================================
else:
    user_text = st.text_input("Type your question")

    if st.button("Ask") and user_text.strip():
        ai_text = get_ai_response(user_text)

        st.session_state.history.append(("You", user_text))
        st.session_state.history.append(("AI", ai_text))

        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
            speech_path = f.name

        with client.audio.speech.with_streaming_response.create(
            model="gpt-4o-mini-tts",
            voice="alloy",
            input=ai_text,
        ) as response:
            response.stream_to_file(speech_path)
        
        st.markdown("**🔊 Sahil’s Response**")
        st.audio(speech_path)


# =====================================================
# 🧠 CONVERSATION HISTORY
# =====================================================
st.divider()
st.subheader("Conversation")

for role, msg in st.session_state.history:
    if role == "You":
        # USER → RIGHT (green bubble)
        st.markdown(
            f"""
            <div style="display:flex; justify-content:flex-end; margin:10px 0;">
                <div style="
                    background-color:#DCF8C6;
                    color:#000000;
                    padding:12px 16px;
                    border-radius:16px;
                    max-width:65%;
                    text-align:right;
                    font-size:15px;
                ">
                    <strong>You:</strong><br>{msg}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        # AI → LEFT (dark bubble, high contrast)
        st.markdown(
            f"""
            <div style="display:flex; justify-content:flex-start; margin:10px 0;">
                <div style="
                    background-color:#2B2B2B;
                    color:#FFFFFF;
                    padding:12px 16px;
                    border-radius:16px;
                    max-width:65%;
                    font-size:15px;
                ">
                    <strong>Sahil:</strong><br>{msg}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
