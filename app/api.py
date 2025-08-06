from flask import Flask, request, jsonify
from flasgger import Swagger
import redis
import json
from app.ai_service import responder_com_tinyllama
from app.storage import (
    save_message_pair,
    save_error,
    get_last_messages,
    get_last_errors
)

app = Flask(__name__)
swagger = Swagger(app)

# Conexão com Redis
redis_client = redis.Redis(host='redis-server', port=6379, db=0, decode_responses=True)

@app.route('/send-message', methods=['POST'])
def send_message():
    """
    Desenvolvimento de end point para UI cadastro.
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
              example: "+5575998034205"
            message:
              type: string
              example: "Quero saber sobre meus débitos"
    responses:
      200:
        description: Mensagem recebida e enviada para processamento
      400:
        description: Dados inválidos
    """
    data = request.get_json()
    if not data or 'to' not in data or 'message' not in data:
        return jsonify({'error': 'Parâmetros inválidos'}), 400

    try:
        redis_client.rpush('message_queue', json.dumps(data))
        return jsonify({
            'status': 'Mensagem recebida com sucesso',
            'detalhe': 'Ela será processada em segundo plano.'
        }), 200
    except Exception as e:
        return jsonify({
            'status': 'Erro ao enfileirar a mensagem',
            'erro': str(e)
        }), 500

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
