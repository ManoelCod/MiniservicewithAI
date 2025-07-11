# 💬 MiniservicewithAI

Um microserviço inteligente que responde automaticamente a mensagens de clientes sobre débitos, utilizando IA com TinyLlama, Redis para fila de mensagens, SQLite para histórico e integração com WhatsApp.

## ✅ Requisitos

Antes de executar a aplicação, certifique-se de ter os seguintes componentes instalados:

### 🧰 Dependências locais

- [Python 3.10+](https://www.python.org/)
- [pip](https://pip.pypa.io/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Redis](https://hub.docker.com/_/redis) rodando em container
- [Ollama](https://ollama.com/) com modelo TinyLlama

### Serviços em segundo plano

```bash
docker run -d --name miniservice_redis -p 6379:6379 redis:7
docker run -d --name miniservice_ollama -p 11434:11434 ollama/ollama
```

Depois de subir o container do Ollama, entre nele e ative o modelo:
```bash
docker exec -it miniservice_ollama bash
ollama run tinyllama
```

## 🚀 Funcionalidades

- 🔁 Enfileiramento de mensagens com Redis
- 🤖 Respostas automáticas com IA (TinyLlama via Ollama)
- 🧾 Consulta de débitos por número de telefone
- 🗃️ Armazenamento de histórico e erros em SQLite
- 📊 Documentação interativa com Swagger (Flasgger)
- 🛠️ Worker assíncrono para processar mensagens em segundo plano
- 💬 Integração com WhatsApp para envio e recebimento de mensagens

---

## 🧱 Estrutura do Projeto

- `app/` - Código principal do microserviço
- `run.py` - Inicialização do servidor Flask
- `app/worker.py` - Worker assíncrono para processamento de mensagens
- `app/storage.py` - Inicialização e manipulação do banco SQLite
- `requirements.txt` - Dependências Python
- `Dockerfile` e `supervisord.conf` - Arquivos para containerização e supervisão
- `README.md` - Documentação do projeto

---

## ⚙️ Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/MiniservicewithAI.git
cd MiniservicewithAI
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Inicialize o banco de dados

```bash
python -c "from app.storage import init_db; init_db()"
```

### 4. Inicie o servidor Flask

```bash
python run.py
```

### 5. Inicie o worker

```bash
python -m app.worker
```

---

## 📲 Integração com WhatsApp

O projeto possui integração para envio e recebimento de mensagens via WhatsApp.  
**Limitações importantes:**
- Não é possível clicar no botão de envio automaticamente (via script), pois o WhatsApp bloqueia interações automatizadas por políticas de segurança.
- Também não é possível acessar ou ler mensagens via JavaScript puro no WhatsApp Web — isso requer automação com ferramentas como Selenium ou Puppeteer (e mesmo assim é frágil).

---

## 🔗 Observação

É possível integrar via API com outras plataformas de mensagens, desde que o serviço ofereça recursos para automação e integração semelhantes aos do WhatsApp.





