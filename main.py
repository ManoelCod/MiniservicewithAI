from openai import OpenAI, OpenAIError
from llama_cpp import Llama
import os

# Inicializa cliente OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Inicializa TinyLlama local
tinyllama = Llama(
    model_path="models/tinyllama-1.1b-chat.q4_K_M.gguf",
    n_ctx=512,
    n_threads=4
)

def generate_response(user_message: str) -> str:
    try:
        # Tenta usar OpenAI
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um atendente virtual simpático."},
                {"role": "user", "content": user_message}
            ]
        )
        return response.choices[0].message.content.strip()

    except OpenAIError as e:
        print("⚠️ OpenAI falhou, usando TinyLlama:", e)

        # Usa TinyLlama local como fallback
        prompt = f"[INST] {user_message} [/INST]"
        output = tinyllama(prompt, max_tokens=200, temperature=0.7)
        return output["choices"][0]["text"].strip()