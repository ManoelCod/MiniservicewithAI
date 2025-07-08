from app.dados_simulados import debito_por_numero

def gerar_prompt_para_ia(numero: str) -> str:
    if numero in debito_por_numero:
        valores = debito_por_numero[numero]
        total = sum(valores)
        lista = ", ".join(f"R$ {v:.2f}" for v in valores)
        return (
            f"Cliente {numero} possui débitos: {lista}. Total: R$ {total:.2f}. "
            f"Responda de forma educada e objetiva em 1 linha."
        )
    else:
        return (
            f"Cliente {numero} não possui débitos. "
            f"Responda de forma educada e objetiva em 1 linha."
        )