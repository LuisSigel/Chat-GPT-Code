from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()  # loads .env into environment
api_key = os.getenv("open_api_key")
# Replace with your real API key
client = OpenAI(api_key=api_key) # Initialize the OpenAI client with the API key

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "developer", "content": "You are a helpful assistant."}, #GPT role
        {"role": "user", "content": "Write a one-sentence bedtime story about a unicorn."} #user role
        #addfunctions = Here, add additional functions apart from model and messages. E.g. Temperature, presence penalty, repsonse format, store(only then requests are stored)..See documentation
    ]
)

print(completion.choices[0].message.content) #choices[] which answer to take (by default you only get one); message.content means only the content is the output.