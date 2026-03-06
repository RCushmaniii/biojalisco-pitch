import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Completion.create(
    model="gpt-3.5-turbo-instruct",
    prompt="Say hello to the world!",
    max_tokens=20
)

print(response.choices[0].text.strip())
