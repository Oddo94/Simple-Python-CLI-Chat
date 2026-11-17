# Implement the Python code using the `openai` library to create the assistant.
# Start with a system prompt for the chat completion API.
# Send a static message and receive a response from the API.
# Show the chat completion message.
from openai import OpenAI

import os
from dotenv import load_dotenv

load_dotenv()


def get_openai_client():
    client = OpenAI(
        api_key=os.getenv("OPENAI_API_KEY"),
        base_url=os.getenv("OPENAI_BASE_URL")
        )

    return client


def query_openai_client(input_query):
    response = get_openai_client().responses.create(
        model="gpt-4o-mini",
        input = [
            {"role": "system", "content": "You are a helpful assistant for a simple CLI chat. Only respond with text messages. Get creative with the answers!"},
            {"role": "user", "content": input_query}
        ]
    )

    return response


def calculate_query_cost(input_tokens, input_token_price,  output_tokens, output_token_price):
    measuring_unit = 1_000_000
    input_tokens_cost = (input_token_price / measuring_unit) * input_tokens
    output_tokens_cost = (output_token_price / measuring_unit) * output_tokens

    total_cost = input_tokens_cost + output_tokens_cost

    return f"{total_cost:.7f}"


def get_openai_response(input_query):
    return query_openai_client(input_query)


def start_chat_session():
    user_input = input("Enter a message:")
    print(f"You: {user_input}")

    ai_response = get_openai_response(user_input)

    input_token_price = 0.15
    output_token_price = 0.60
    input_tokens = ai_response.usage.input_tokens
    output_tokens = ai_response.usage.output_tokens
    ai_query_cost = calculate_query_cost(input_tokens, input_token_price, output_tokens, output_token_price)

    print(f"Assistant: {ai_response.output_text}")
    print(f"Cost: ${ai_query_cost}")


start_chat_session()




