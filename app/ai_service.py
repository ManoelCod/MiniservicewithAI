from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_response(user_message):
    response = client.chat.completions.create(
        model="gpt-4.1",  # ou "gpt-4", "gpt-4o", etc.
        messages=[
            {"role": "system", "content": "Você é um atendente virtual simpático e prestativo."},
            {"role": "user", "content": user_message}
        ]
    )
    return response.choices[0].message.content.strip()