import redis, json, traceback, time
import json
from ai_service import generate_response
from storage import save_message_pair, save_error


r = redis.Redis(host='localhost', port=6379, db=0)


print("Worker iniciado.")

while True:
    # tenta por até 5 segundos e retorna None se não houver item
    item = r.blpop('message_queue', timeout=5)
    if not item:
        print("Sem mensagens. Continuo aguardando...")
        continue

    _, message_json = item
    data = json.loads(message_json)
    phone = data['to']
    user_message = data['message']

    try:
        ai_response = generate_response(user_message)
        save_message_pair(phone, user_message, ai_response)
        print(f"[{phone}] IA: {ai_response}")

    except Exception as e:
        tb = traceback.format_exc()
        print(f"[{phone}] Erro:\n{tb}")
        save_error(phone, user_message, str(e))
        fallback = "Desculpe, não consegui processar sua solicitação."
        save_message_pair(phone, user_message, fallback)
