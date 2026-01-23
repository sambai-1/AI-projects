import os
from openai import OpenAI
import asyncio
from cloud_models import env
os.environ["OPENAI_API_KEY"] = env.OPENAI_API_KEY

from pydantic import BaseModel
from agents import (
    Agent,
    GuardrailFunctionOutput,
    InputGuardrailTripwireTriggered,
    RunContextWrapper,
    Runner,
    TResponseInputItem,
    input_guardrail,
)



class HomeworkOutput(BaseModel):
    is_homework: bool
    reasoning: str

guardrail_agent = Agent(
    name="Guardrail check",
    instructions="Check if the user is asking about homework.",
    output_type=HomeworkOutput,
)

history_tutor_agent = Agent(
    name="History Tutor",
    handoff_description="Specialist agent for historical questions",
    instructions="You provide assistance with historical queries. Explain important events and context clearly.",
)

math_tutor_agent = Agent(
    name="Math Tutor",
    handoff_description="Specialist agent for math questions",
    instructions="You provide help with math problems. Explain your reasoning at each step and include examples",
)

@input_guardrail(run_in_parallel=False)
async def homework_guardrail( 
    ctx: RunContextWrapper[None], agent: Agent, input: str | list[TResponseInputItem]) -> GuardrailFunctionOutput:

    result = await Runner.run(guardrail_agent, input, context=ctx.context)

    return GuardrailFunctionOutput(
        output_info=result.final_output, 
        tripwire_triggered=not result.final_output.is_homework,
    )


allocator_agent = Agent(
    name="Allocator Agent",
    instructions="You determine which agent to use based on the user's homework question",
    handoffs=[history_tutor_agent, math_tutor_agent],
    input_guardrails=[homework_guardrail]
)


async def main():
    # turns out what is 2 + 2 is not homework :skull:
    result = await Runner.run(allocator_agent, "Can you help me with my homework? what is 2 + 2")
    print(result.final_output)


    try:
        result = await Runner.run(allocator_agent, "Should I buy apples or oranges")
        print(result.final_output)
    except InputGuardrailTripwireTriggered as e:
        print("Guardrail blocked this input:", e)


if __name__ == "__main__":
    asyncio.run(main())