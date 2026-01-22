import os
from openai import OpenAI
from dotenv import load_dotenv
from agents import Agent, Runner
import asyncio


# this does not work, try with open webui next time

local_client = OpenAI(
    base_url = 'http://localhost:11434/v1',
    api_key='ollama'
)

os.environ["OPENAI_API_KEY"] = "http://localhost:11434/v1"



spanish_agent = Agent(
    name="Spanish Agent",
    model="gwen3:8b",
    instructions="You translate text to Spanish."
)

french_agent = Agent(
    name="French Agent",
    model="gwen3:8b",
    instructions="You translate text to French."
)

italian_agent = Agent(
    name="Italian Agent",
    model="gwen3:8b",
    instructions="You translate text to Italian."
)

manager_agent = Agent(
    name="Manager Agent",
    model="gwen3:8b",
    instructions=(
        "You are a translation manager. "
        "If the user asks for translations, you call the right tools. "
        "Always return the translations clearly."
    ),
    
    tools=[
        spanish_agent.as_tool(
            tool_name="translate_to_spanish",
            tool_description="Translate the user's message to Spanish"
        ),
        french_agent.as_tool(
            tool_name="translate_to_french",
            tool_description="Translate the user's message to French"
        ),
        italian_agent.as_tool(
            tool_name="translate_to_italian",
            tool_description="Translate the user's message to Italian"
        ),
    ],
)


async def main():
    msg = "Translate 'hello' into Spanish, French, and Italian"
    
    orchestrator_output = await Runner.run(
        manager_agent, 
        msg,

    )

    print("\n=== Final Answer ===")
    print(orchestrator_output.final_output)

if __name__ == "__main__":
    asyncio.run(main())

