import os
from openai import AsyncOpenAI
from agents import Agent, Runner, OpenAIChatCompletionsModel, RunConfig
from dotenv import load_dotenv
load_dotenv()

gemini_api_key = os.getenv('GEMINI_API_KEY')

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY environment variable is not set.")


external_client = AsyncOpenAI(
    api_key = gemini_api_key,
    base_url = 'https://generativelanguage.googleapis.com/v1beta/openai/',
)

model = OpenAIChatCompletionsModel(
    model = 'gemini-2.0-flash',
    openai_client = external_client,
)

config = RunConfig(
    model = model,
    model_provider = external_client,
    tracing_disabled = True,
)

writer = Agent(
    name = 'Writer',
    instructions = 'You are a helpful writer agent.'
)

prompt = input("Enter your prompt: ")

response = Runner.run_sync(
    writer,
    prompt,
    run_config = config
)
print("Response from Writer Agent:")
print(response.final_output)