import os
import env
import time
from openai import OpenAI
from agents import Agent, Runner, ModelSettings

os.environ["OPENAI_API_KEY"] = env.OPENAI_API_KEY


agent = Agent(
    name="Assistant", 
    instructions="You are a helpful assistant",
    model="gpt-5-nano",
    model_settings=ModelSettings(
        extra_args={"service_tier": "flex"},
    ),
)

result = Runner.run_sync(agent, "Write a haiku about recursion in programming.")

print(result.raw_responses)
print(result.final_output)