import os
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig
from dotenv import load_dotenv



load_dotenv()
gemini_api_key = os.getenv('GEMINI_API_KEY')

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY environment variable is not set.")


external_client = AsyncOpenAI(
    api_key = gemini_api_key,
    base_url = 'https://generativelanguage.googleapis.com/v1beta',
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

response = Runner.run_sync(
    writer,
    input = "give me some Love poetry. roman english me likh kar do..",
    run_config = config
)
print("Response from Writer Agent:")
print(response)