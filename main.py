# Implement the Python code using the `openai` library to create the assistant.
# Start with a system prompt for the chat completion API.
# Send a static message and receive a response from the API.
# Show the chat completion message.
from openai import OpenAI

import os
from dotenv import load_dotenv



#print('Hello, World!')

load_dotenv()
#print(os.getenv("OPENAI_API_KEY"))


def get_openai_client():
    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("OPENAI_BASE_URL")
        )

    return client

def query_openai_client():
    response = get_openai_client().responses.create(
        model="gpt-4o-mini",
        input = [
            {"role": "system", "content": "You are a helpful assistant for a simple CLI chat. Only respond with text messages. Get creative with the answers!"},
            {"role": "user", "content": "What are you?"}
        ]
    )

    return response

def get_openai_response():
    print(query_openai_client().output_text)

#print(get_openai_client().api_key)
get_openai_response()




