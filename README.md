# 💬 MiniservicewithAI

Um microserviço inteligente que responde automaticamente a mensagens de clientes sobre débitos, utilizando IA com TinyLlama, Redis para fila de mensagens e SQLite para histórico.

---

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





