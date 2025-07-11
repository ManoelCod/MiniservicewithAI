import asyncio
import subprocess
import time

async def usar_copilot(prompt):
    comando = ["gh", "copilot", "suggest", prompt]
    start = time.time()
    process = await asyncio.create_subprocess_exec(
        *comando,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
        # Remover text=True
    )

    print("⏳ Processando...", end="", flush=True)
    percent = 0
    while True:
        if process.returncode is not None:
            break
        await asyncio.sleep(0.2)
        percent = min(percent + 5, 95)
        print(f"\r⏳ Processando... {percent}%", end="", flush=True)
        if process.stdout.at_eof():
            break

    stdout, stderr = await process.communicate()
    elapsed = time.time() - start
    print(f"\r⏳ Processando... 100%")
    print(f"⏱️ Tempo de resposta: {elapsed:.2f}s")

    # Decodificar a saída
    stdout = stdout.decode('utf-8') if stdout else ''
    stderr = stderr.decode('utf-8') if stderr else ''

    if process.returncode == 0:
        return stdout
    else:
        return f"❌ Erro: {stderr}"

def main():
    print("🚀 Terminal Copilot. Digite um comando ou pergunta.")
    while True:
        entrada = input("📥 Você: ")
        if entrada.lower() in ["sair", "exit", "quit"]:
            break
        resposta = asyncio.run(usar_copilot(entrada))
        print("🤖 Copilot respondeu:\n")
        print(resposta)

if __name__ == "__main__":
    main()