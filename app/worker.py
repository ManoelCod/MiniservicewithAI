import redis
import json
from ai_service import generate_response
from storage import save_message_pair

redis_client = redis.Redis(host='localhost', port=6379, db=0)

print("Worker iniciado. Aguardando mensagens...")

while True:
    _, message_json = redis_client.blpop('message_queue')
    message_data = json.loads(message_json)

    user_message = message_data['message']
    to = message_data['to']

    # Gera resposta com IA
    ai_response = generate_response(user_message)

    # Salva no histórico
    save_message_pair(to, user_message, ai_response)

    print(f"[{to}] Cliente: {user_message}")
    print(f"[{to}] IA: {ai_response}")