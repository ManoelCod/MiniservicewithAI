# 💬 MiniservicewithAI

Um microserviço inteligente que responde automaticamente a mensagens de clientes sobre débitos, utilizando IA com TinyLlama, Redis para fila de mensagens e SQLite para histórico.

## ✅ Requisitos

Antes de executar a aplicação, certifique-se de ter os seguintes componentes instalados:

### 🧰 Dependências locais

- [Python 3.10+](https://www.python.org/)
- [pip](https://pip.pypa.io/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### Serviço em segundo plano

docker run -d --name miniservice_redis -p 6379:6379 redis:7

### Ollama com TinyLlama
docker run -d --name miniservice_ollama -p 11434:11434 ollama/ollama

Depois de subir o container, entre nele e ative o modelo:
docker exec -it miniservice_ollama bash
ollama run tinyllama

## 🚀 Funcionalidades

- 🔁 Enfileiramento de mensagens com Redis
- 🤖 Respostas automáticas com IA (TinyLlama via Ollama)
- 🧾 Consulta de débitos por número de telefone
- 🗃️ Armazenamento de histórico e erros em SQLite
- 📊 Documentação interativa com Swagger (Flasgger)
- 🛠️ Worker assíncrono para processar mensagens em segundo plano

---

## 🧱 Estrutura do Projeto


---

## ⚙️ Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/MiniservicewithAI.git
cd MiniservicewithAI

pip install -r requirements.txt

python -c "from app.storage import init_db; init_db()"

4. Inicie o servidor Flask
python run.py

Inicie o worker 
python -m app.worker





