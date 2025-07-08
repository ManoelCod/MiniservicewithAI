from flask import Flask, request, jsonify
from flasgger import Swagger
import redis
import json
from app.storage import get_last_messages,get_last_errors


app = Flask(__name__)
swagger = Swagger(app)

# Conexão com Redis
redis_client = redis.Redis(host='localhost', port=6379, db=0)

@app.route('/send-message', methods=['POST'])
def send_message():
    """
    Envia uma mensagem do cliente para a fila
    ---
    tags:
      - Mensagens
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - to
            - message
          properties:
            to:
              type: string
              example: "+5511999999999"
            message:
              type: string
              example: "Quero saber sobre meus débitos"
    responses:
      200:
        description: Mensagem enfileirada com sucesso
      400:
        description: Dados inválidos
    """
    data = request.get_json()
    if not data or 'to' not in data or 'message' not in data:
        return jsonify({'error': 'Parâmetros inválidos'}), 400

    redis_client.rpush('message_queue', json.dumps(data))
    return jsonify({'status': 'Mensagem enviada para processamento'}), 200

@app.route('/history', methods=['GET'])
def history():
    """
    Retorna as últimas 10 mensagens trocadas com a IA
    ---
    tags:
      - Histórico
    responses:
      200:
        description: Lista de mensagens
    """
    messages = get_last_messages(10)
    return jsonify(messages), 200

@app.route('/errors', methods=['GET'])
def errors():
    """
    Lista os últimos 10 erros capturados
    ---
    tags:
      - Erros
    responses:
      200:
        description: Lista de erros
    """
    return jsonify(get_last_errors(10)), 200
