from app.dados_simulados import debito_por_numero
import requests

def gerar_prompt_para_ia(numero: str) -> str:
    if numero in debito_por_numero:
        valores = debito_por_numero[numero]
        total = sum(valores)
        lista = ", ".join(f"R$ {v:.2f}" for v in valores)
        return (
            f"{numero}: débitos {lista} (total R$ {total:.2f}). "
            f"Resuma em 1 linha os débitos para número {numero}."
        )
    else:
        return (
            f"{numero}: nenhum débito encontrado. "
            f"Responda em 1 linha com educação se o débido não foi encontrado."
        )

def gerar_link_whatsapp(numero: str, mensagem: str) -> str:
    return f"https://wa.me/{numero}?text={requests.utils.quote(mensagem)}"        