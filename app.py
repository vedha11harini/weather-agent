import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

from tools import get_weather
from prompts import SYSTEM_PROMPT

# Load environment variables
load_dotenv()

# Create Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

MODEL = os.getenv("MODEL")

# Streamlit page config
st.set_page_config(
    page_title="AI Weather Agent",
    page_icon="🌤️",
    layout="centered"
)

st.title("🌤️ AI Weather Agent")
st.write("Ask me about the weather anywhere in the world!")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
user = st.chat_input("Enter your question...")

if user:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user
        }
    )

    with st.chat_message("user"):
        st.markdown(user)

    try:

        prompt = f"""
{SYSTEM_PROMPT}

If the user asks about weather, temperature, climate, humidity, rainfall etc.

Reply ONLY in this format:

CALL_WEATHER:<city>

Example:
CALL_WEATHER:Coimbatore

Otherwise answer normally.

User:
{user}
"""

        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        answer = response.choices[0].message.content.strip()

        # Tool calling
        if answer.startswith("CALL_WEATHER:"):

            city = answer.replace("CALL_WEATHER:", "").strip()

            weather = get_weather(city)

            final_prompt = f"""
The user asked:

{user}

Weather Information:

{weather}

Explain this weather in a friendly and easy-to-understand way.

Do not mention JSON.
"""

            final = client.chat.completions.create(
                model=MODEL,
                messages=[
                    {
                        "role": "user",
                        "content": final_prompt
                    }
                ]
            )

            final_answer = final.choices[0].message.content

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

    except Exception as e:
        st.error(f"Error: {e}")