from flask import Flask, request, jsonify
import redis
import json
from storage import get_last_messages

app = Flask(__name__)

# Conexão com Redis
redis_client = redis.Redis(host='localhost', port=6379, db=0)

@app.route('/send-message', methods=['POST'])
def send_message():
    data = request.get_json()
    if not data or 'to' not in data or 'message' not in data:
        return jsonify({'error': 'Parâmetros inválidos'}), 400

    # Enfileira a mensagem no Redis
    redis_client.rpush('message_queue', json.dumps(data))
    return jsonify({'status': 'Mensagem enviada para processamento'}), 200

@app.route('/history', methods=['GET'])
def history():
    messages = get_last_messages(10)
    return jsonify(messages), 200