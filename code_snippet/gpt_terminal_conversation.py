import os
import openai

openai.api_key = os.environ["OPEN_AI_API_KEY"]

def send_message(message_log):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message_log,
        temperature=0.5,
    )

    for choice in response.choices:
        if "text" in choice:
            return choice.text
