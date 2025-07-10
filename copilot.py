import subprocess

def usar_copilot(prompt):
    comando = ["gh", "copilot", "suggest", prompt]
    resultado = subprocess.run(comando, capture_output=True, text=True)

    if resultado.returncode == 0:
        return resultado.stdout
    else:
        return f"❌ Erro: {resultado.stderr}"

def main():
    print("🚀 Terminal Copilot. Digite um comando ou pergunta.")
    while True:
        entrada = input("📥 Você: ")
        if entrada.lower() in ["sair", "exit", "quit"]:
            break
        resposta = usar_copilot(entrada)
        print("🤖 Copilot respondeu:\n")
        print(resposta)

if __name__ == "__main__":
    main()