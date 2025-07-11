# from openai import OpenAI, OpenAIError  # ← Desativado: OpenAI não será usado devido quantidade de cotas da Api.
import requests
from requests.exceptions import Timeout, RequestException
from app.function import gerar_prompt_para_ia
from app.dados_simulados import debito_por_numero


# Se quiser reativar futuramente:
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Endpoint local do Ollama
OLLAMA_URL = "http://ollama:11434/api/generate"
OLLAMA_MODEL = "phi"


def responder_com_tinyllama(numero: str) -> str:
    prompt = gerar_prompt_para_ia(numero)

    try:
        res = requests.post(
            OLLAMA_URL,
            json={
                "model": OLLAMA_MODEL,
                "prompt": prompt,
                "stream": False
            },
            timeout=60  # ⏱️ tempo limite de 30 segundos
        )
        res.raise_for_status()

        resposta = res.json().get("response", "").strip()

        # Se a IA responder vazio ou irrelevante, usamos resposta pronta
        if not resposta or resposta.lower() in ["artificial intelligence", ""]:
            print("⚠️ Resposta vazia ou genérica, usando resposta pronta.")
            return gerar_resposta_pronta(numero)

        return resposta

    except Timeout:
        return gerar_resposta_pronta(numero)

    except RequestException as e:
        print(f"❌ Falha ao consultar modelo IA: {e}")
        return f"Desculpe, houve uma falha na consulta. Tente novamente mais tarde . {e}"

def gerar_resposta_pronta(numero: str) -> str:
    if numero in debito_por_numero:
        valores = debito_por_numero[numero]
        total = sum(valores)
        lista = ", ".join(f"R$ {v:.2f}" for v in valores)
        return f"Olá! O cliente {numero} possui débitos: {lista}. Total: R$ {total:.2f}."
    else:
        return f"Olá! O cliente {numero} não possui débitos registrados no momento."
