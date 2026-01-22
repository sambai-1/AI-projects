import asyncio
import os
from cloud_models import env

os.environ["OPENAI_API_KEY"] = env.OPENAI_API_KEY
from agents import Agent, Runner, function_tool, ModelSettings


@function_tool
def get_weather(city: str) -> str:
    return "bob"
    return f"The weather in {city} is sunny."


agent = Agent(
    name="Hello world",
    instructions="You are a helpful agent.",
    tools=[get_weather],
)


async def main():
    result = await Runner.run(agent, input="What's the weather in Tokyo?")
    print(result.final_output)
    # The weather in Tokyo is sunny.


if __name__ == "__main__":
    asyncio.run(main())