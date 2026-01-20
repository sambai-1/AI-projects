import os
import env
import time
from openai import OpenAI
from agents import Agent, Runner, ModelSettings

# Inject it into the environment manually
os.environ["OPENAI_API_KEY"] = env.OPENAI_API_KEY

"""
client = OpenAI()
start_time = time.time()

response = client.responses.create(
    model="gpt-5-nano",
    input="Write a one-sentence bedtime story about a unicorn.",
    service_tier="flex"
)
end_time = time.time()

print(f"Client Output: {response.output_text}")
print(f"Client Time: {end_time - start_time:.2f} seconds\n")
"""

'''
# 2. Attach these settings to your Agent
agent = Agent(
    name="Assistant", 
    instructions="You are a helpful assistant",
    model="gpt-5-nano",
    model_settings=ModelSettings(
        extra_args={"service_tier": "flex"},
    ),
)

start_time = time.time()
result = Runner.run_sync(agent, "Write a haiku about recursion in programming.")
end_time = time.time()

print(f"Agent Output: {result.final_output}")
print(f"Agent Command took: {end_time - start_time:.2f}")
'''