import os
from dotenv import load_dotenv
from openai import OpenAI
import argparse


load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()

if api_key is None:
    raise RuntimeError("OpenRouter key is not found") 

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

messages=[
    {
        "role": "user",
        "content": args.user_prompt,
    }
]

response = client.chat.completions.create(
                model = "openrouter/free",
                messages = messages    
            )
if args.verbose:
    print(f"User prompt: {args.user_prompt}")
    print(f"Prompt tokens: {response.usage.prompt_tokens}")
    print(f"Response tokens: {response.usage.completion_tokens}")
print("Response:")
print(response.choices[0].message.content)
