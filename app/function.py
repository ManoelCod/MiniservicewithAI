from app.dados_simulados import debito_por_numero

def gerar_prompt_para_ia(numero: str) -> str:
    if numero in debito_por_numero:
        valores = debito_por_numero[numero]
        total = sum(valores)
        lista = ", ".join(f"R$ {v:.2f}" for v in valores)
        return f"""
Você é um assistente financeiro simpático. Um cliente entrou em contato perguntando sobre seus débitos.

Número do cliente: {numero}
Débitos encontrados: {lista}
Total em aberto: R$ {total:.2f}

Responda de forma educada e clara, como se estivesse falando com o cliente.
"""
    else:
        return f"""
Você é um assistente financeiro simpático. Um cliente entrou em contato perguntando sobre seus débitos.

Número do cliente: {numero}
Nenhum débito foi encontrado.

Responda de forma educada e clara, informando que não há débitos registrados.
"""