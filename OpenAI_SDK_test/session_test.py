
import os
import asyncio
from openai import OpenAI
from cloud_models import env
os.environ["OPENAI_API_KEY"] = env.OPENAI_API_KEY
from agents import Agent, Runner, SQLiteSession

async def main():
    agent = Agent(name="Assistant", instructions="Reply concisely.")
    
    session = SQLiteSession("user_123", "session_conversations.db")

    # previously i put in message "Hi, my name is bob"
    result1 = await Runner.run(agent, "Can you repeat my name back to me?", session=session)
    print(result1.final_output)


if __name__ == "__main__":
    asyncio.run(main())