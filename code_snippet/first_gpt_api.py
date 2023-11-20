import os
import openai

openai.api_key = os.environ["OPEN_AI_API_KEY"]


def ask_to_gpt_35_turbo(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        top_p=0.1,
        temperature=0.1,
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": user_input}
        ]
    )

    return response.choices[0].message.content

users_request = """
인기 있는 프로그래밍 언어: 한국과 미국을 구별하여, 상위 15개
"""

r=ask_to_gpt_35_turbo(users_request)
print(r)


