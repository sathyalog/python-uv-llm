from dotenv import load_dotenv
import os
import sys
import asyncio
import httpx
from groq import Groq, AsyncGroq

load_dotenv(override=True)

async def main():
    client = AsyncGroq(api_key=os.getenv("GROQ_API_KEY"))
    model_id = os.getenv("MODEL")
    prompts = [
        "Write a short poem about the ocean.",
        "Explain the theory of relativity in simple terms.",
        "What are the benefits of meditation?",
    ]
    async def ask(prompt):
        response = await client.chat.completions.create(
            model=model_id,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    
    results = await asyncio.gather(*(ask(p) for p in prompts))

    for res in results:
        print(res)


if __name__ == "__main__":
    asyncio.run(main())
