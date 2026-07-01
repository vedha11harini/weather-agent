import os

from dotenv import load_dotenv

from google import genai

from tools import get_weather

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GROQ_API_KEY")
)

MODEL = os.getenv("MODEL")

print("Model :", MODEL)

while True:

    user = input("\nYou : ")

    if user.lower() == "exit":
        break

    prompt = f"""
You are a Weather Agent.

If the user asks for weather,
reply ONLY with:

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

Weather Data:

{weather}

Explain it nicely.
"""
        )

        print("\nAssistant :")
        print(final.text)

    else:

        print("\nAssistant :")
        print(answer)