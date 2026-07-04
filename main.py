from dotenv import load_dotenv
import os
import sys

import httpx
from groq import Groq, AuthenticationError

load_dotenv(override=True)

def main():
    model = os.getenv("MODEL")
    api_key = os.getenv("GROQ_API_KEY")

    if not model or not api_key:
        print("MODEL and GROQ_API_KEY must be set in the environment variables.")
        sys.exit(1)

    try:
        client = Groq(api_key=api_key)

        while True:
            user_input = input("You: ")
            if user_input.lower() in ["exit", "quit"]:
                print("Exiting the chat.")
                break

            response = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": user_input}]
            )

            print(f"AI: {response.choices[0].message.content}")

    except AuthenticationError as e:
        print(f"Authentication failed: {e}")
        sys.exit(1)
    except httpx.HTTPStatusError as e:
        print(f"HTTP error occurred: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
