import redis, json, traceback, time
import json
from app.ai_service import responder_com_tinyllama
from app.function import gerar_link_whatsapp
from app.storage import save_message_pair, save_error


# Conexão com Redis
redis_client = redis.Redis(host='redis-server', port=6379, db=0, decode_responses=True)

print("👷 Worker iniciado. Aguardando mensagens...")

while True:
    try:
        # Espera por uma nova mensagem na fila
        _, raw_data = redis_client.blpop('message_queue')
        data = json.loads(raw_data)

        numero = data.get("to")
        mensagem = data.get("message", "").lower()

        print(f"📩 Mensagem recebida de {numero}: {mensagem}")

        if "débito" in mensagem:
            resposta = responder_com_tinyllama(numero)
            print(f"🤖 Resposta gerada: {resposta}")

            # Salva histórico da interação
            link = gerar_link_whatsapp(numero, resposta)
            save_message_pair(numero, mensagem, resposta,link)

        else:
            print("⚠️ Mensagem fora do escopo. Ignorada.")

    except Exception as e:
        print("❌ Erro no processamento:", e)
      

    time.sleep(0.5)  # Evita loop acelerado em caso de erro
