import os
from agents import Agent, Runner, RunConfig, AsyncOpenAI, OpenAIChatCompletionsModel
from openai.types.responses import ResponseTextDeltaEvent
from dotenv import load_dotenv
from agents.tool import function_tool
import chainlit as cl # type: ignore
load_dotenv()

gemini_api_key = os.getenv('GEMINI_API_KEY')
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY environment variable is not set.")

# -----Start of OpenAI Client Configuration-----
provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# -----Model Configuration-----
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=provider,
)

# -----Agent Configuration-----
config = RunConfig(
    model=model,
    model_provider=provider,
    tracing_disabled=True,
)

# -----Get Weather Agent Function Initialization-----
@function_tool("get_weather")
def get_weather(location: str, unit:str = "C") -> str:
    print('This is get weather tool call')
    """
    Fetch the weather in a given location, returning a short description.
    """
    return f"The weather in {location} is 22° degree {unit}."

# -----Student Finder Agent Function Initialization-----
@function_tool("giaic_student_finder")
def student_finder(student_roll: int) -> str:
    print('This is student finder tool call')
    """
    Find the GIAIC studnet based on the roll number.
    """
    data = {1:"Qasim", 2:"Ali", 3:"Ahmed", 4:"Sara"}
    return data.get(student_roll, "Student not found.")

# -----Agent Initialization-----
agent = Agent(
    instructions="You are a helpful assistant that can answer questions and perform tasks.",
    name="Support Agent",
    tools=[get_weather, student_finder],
    model=model,
)

@cl.on_chat_start
async def handle_chat_start():
    cl.user_session.set("history", [])
    await cl.Message(content="Hello How can i help you?").send()

@cl.on_message
async def handle_message(message: cl.Message):
    history = cl.user_session.get("history")

    msg = cl.Message(content="")
    await msg.send()

    history.append({"role": "user", "content": message.content})
    result = await Runner.run_streamed(
        agent,
        input=history,
        run_config=config,
    )
    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(
            event.data, ResponseTextDeltaEvent
        ):
            await msg.stream_token(event.data.delta)
            history.append({"role": "assistant", "content": result.final_output})
            cl.user_session.set("history", history)