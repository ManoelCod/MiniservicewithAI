# from openai import OpenAI, OpenAIError  # ← Desativado: OpenAI não será usado devido quantidade de cotas da Api.
import requests
from app.function import gerar_prompt_para_ia
import os

# Se quiser reativar futuramente:
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Endpoint local do Ollama
OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "phi"


def generate_response(user_message: str) -> str:
    try:
        # Usa apenas TinyLlama via API do Ollama
        res = requests.post(OLLAMA_URL, json={
            "model": OLLAMA_MODEL,
            "prompt": user_message,
            "stream": False
        })
        res.raise_for_status()
        return res.json()["response"].strip()

    except Exception as e:
        print("❌ Erro ao usar TinyLlama via Ollama:", e)
        return "Desculpe, não consegui gerar uma resposta no momento."
    
def responder_com_tinyllama(numero: str) -> str:
    prompt = gerar_prompt_para_ia(numero)

    try:
        res = requests.post(OLLAMA_URL, json={
            "model": OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False
        })
        res.raise_for_status()
        return res.json()["response"].strip()

    except Exception as e:
        print("❌ Erro ao usar TinyLlama:", e)
        return "Desculpe, não consegui gerar uma resposta no momento."
    