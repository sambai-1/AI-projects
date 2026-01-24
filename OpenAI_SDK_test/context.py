import os
import asyncio
from openai import OpenAI
from cloud_models import env
os.environ["OPENAI_API_KEY"] = env.OPENAI_API_KEY

from dataclasses import dataclass
from agents import Agent, Runner, function_tool, RunContextWrapper
# function_tool allows a normal python function to register as a tool that an AI can use. 

@dataclass
class UserInfo:
    name: str
    uid: int
    last_purchase: str
    
@function_tool  
async def fetch_user_purchase(wrapper: RunContextWrapper[UserInfo]) -> str:  
    """Fetch the last item the user purchased. Call this function to get user's purchase history."""
    return f"The user {wrapper.context.name} recently purchased a {wrapper.context.last_purchase}."

async def main():
    user_info = UserInfo(name="Sam", uid=1, last_purchase="laptop")

    agent = Agent[UserInfo](  
        name="Assistant",
        instructions="You are a helpful assistant. Use tools if needed.",
        tools=[fetch_user_purchase],
    )

    result = await Runner.run(  
        starting_agent=agent,
        input="What did the user recently purchase?",
        context=user_info,
    )    

    print("\n=== Final Output ===")
    print(result.final_output)      

if __name__ == "__main__":
    asyncio.run(main())