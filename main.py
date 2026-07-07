from dotenv import load_dotenv
import os
import sys
import asyncio
import httpx
from groq import Groq, AsyncGroq

load_dotenv(override=True)
client = AsyncGroq(api_key=os.getenv("GROQ_API_KEY"))
model_id = os.getenv("MODEL")
async def ask(prompt):
        response = await client.chat.completions.create(
            model=model_id,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content

async def main():
    
    prompts = [
        "Tell me a small joke.",
        "Capital of India?",
        "what is 2+2?",
    ]
    
    results = await asyncio.gather(*(ask(p) for p in prompts))
    for res in results:
        print(res)


if __name__ == "__main__":
    asyncio.run(main())
