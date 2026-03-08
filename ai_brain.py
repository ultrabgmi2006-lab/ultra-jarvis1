import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def ask_ai(prompt):

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role":"user","content":prompt}
        ]
    )

    return response.choices[0].message.content
