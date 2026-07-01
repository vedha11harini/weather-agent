import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

from prompts import SYSTEM_PROMPT
from tools import get_weather

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

MODEL = os.getenv("MODEL")

st.set_page_config(
    page_title="AI Weather Agent",
    page_icon="🌤️",
    layout="centered"
)

st.title("🌤️ AI Weather Agent")
st.write("Ask me about the weather anywhere in the world!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user = st.chat_input("Ask your question...")

if user:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user
        }
    )

    with st.chat_message("user"):
        st.markdown(user)

    prompt = f"""
{SYSTEM_PROMPT}

If the user asks for weather,
reply ONLY like this:

CALL_WEATHER:<city>

Otherwise answer normally.

User:
{user}
"""

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )

    answer = response.text.strip()

    if answer.startswith("CALL_WEATHER:"):

        city = answer.replace("CALL_WEATHER:", "").strip()

        weather = get_weather(city)

        final = client.models.generate_content(
            model=MODEL,
            contents=f"""
User asked:

{user}

Weather Information:

{weather}

Explain it in a friendly way.
"""
        )

        final_answer = final.text

    else:

        final_answer = answer

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": final_answer
        }
    )

    with st.chat_message("assistant"):
        st.markdown(final_answer)