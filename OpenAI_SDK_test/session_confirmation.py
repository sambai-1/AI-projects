import os
import asyncio
from openai import OpenAI
from cloud_models import env
os.environ["OPENAI_API_KEY"] = env.OPENAI_API_KEY
from agents import Agent, Runner, SQLiteSession

async def main():
    
    session = SQLiteSession("user_123", "session_conversations.db")
    items = await session.get_items()
    print(f"Total messages in database: {len(items)}")

    for item in items:
        print(f"[{item['role']}]: {item['content'][:50]}...")


if __name__ == "__main__":
    asyncio.run(main())