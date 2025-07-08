from app.dados_simulados import debito_por_numero

def gerar_prompt_para_ia(numero: str) -> str:
    if numero in debito_por_numero:
        valores = debito_por_numero[numero]
        total = sum(valores)
        lista = ", ".join(f"R$ {v:.2f}" for v in valores)
        return (
            f"{numero}: débitos {lista} (total R$ {total:.2f}). "
            f"Resuma em 1 linha com educação."
        )
    else:
        return (
            f"{numero}: nenhum débito encontrado. "
            f"Responda em 1 linha com educação."
        )