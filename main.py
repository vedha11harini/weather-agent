import os
from dotenv import load_dotenv
from groq import Groq

from tools import get_weather

# Load .env file
load_dotenv()

# Create Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

MODEL = os.getenv("MODEL")

print("====================================")
print("🌤️ AI Weather Agent Started")
print("Model :", MODEL)
print("Type 'exit' to quit")
print("====================================")

while True:

    user = input("\nYou : ")

    if user.lower() == "exit":
        print("\nGoodbye 👋")
        break

    # First prompt: decide whether weather tool is needed
    prompt = f"""
You are an AI Weather Agent.

If the user asks about weather, temperature, climate, rainfall, humidity,
reply ONLY in this format:

CALL_WEATHER:<city>

Examples:
CALL_WEATHER:Coimbatore
CALL_WEATHER:Chennai

Do not write anything else.

If the user is NOT asking about weather,
answer normally.

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

    # Tool Calling
    if answer.startswith("CALL_WEATHER:"):

        city = answer.replace("CALL_WEATHER:", "").strip()

        weather = get_weather(city)

        final_prompt = f"""
The user asked:

{user}

Here is the weather information:

{weather}

Explain this weather information in a friendly, simple way.
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

        print("\nAssistant :")
        print(final_answer)

    else:

        print("\nAssistant :")
        print(answer)