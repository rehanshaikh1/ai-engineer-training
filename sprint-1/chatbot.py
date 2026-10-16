
import json
import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_FILE = BASE_DIR / "llm_request_response.json"

load_dotenv(BASE_DIR / ".env")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENAI_API_KEY")
)

MODEL = os.getenv("OPENAI_MODEL", "google/gemma-4-31B-it")

SYSTEM_PROMPT = """
You are an internal IT support assistant.
Help employees troubleshoot technical issues.
Ask clarifying questions when necessary.
Provide clear, practical troubleshooting steps.
Do not claim that a ticket has been created unless
a connected ticketing system confirms it.
"""


def ask_assistant(message):
    request_payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT.strip()},
            {"role": "user", "content": message}
        ]
    }

    response = client.chat.completions.create(**request_payload)
    response_data = response.model_dump(mode="json")

    capture = {
        "request": request_payload,
        "response": response_data
    }

    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        json.dump(capture, file, indent=2, ensure_ascii=False)

    return response.choices[0].message.content


def main():
    print("Internal IT Support Chatbot")
    print("Type 'exit' to quit.")

    while True:
        message = input("\nYou: ").strip()

        if message.lower() == "exit":
            print("Goodbye!")
            break

        if not message:
            print("Please enter a message.")
            continue

        try:
            answer = ask_assistant(message)
            print("\nIT Support:", answer)
            print(f"\nRequest and response saved to: {OUTPUT_FILE.name}")

        except Exception as error:
            print(f"API request failed: {error}")


if __name__ == "__main__":
    main()
