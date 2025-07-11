# Usa imagem oficial do Python
FROM python:3.11-slim

# Instala dependências básicas e o supervisor
RUN apt-get update && apt-get install -y \
    supervisor \
    procps  # 👉 opcional, adiciona o comando `ps` para depuração

# Define diretório de trabalho
WORKDIR /app

# Copia tudo
COPY . .

# Instala dependências do Python
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Cria diretório de logs (caso ainda não exista)
RUN mkdir -p /var/log/supervisor

# Copia config do supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Expõe a porta do Flask
EXPOSE 5000

# Inicia supervisord em primeiro plano
CMD ["supervisord", "-n", "-c", "/etc/supervisor/conf.d/supervisord.conf"]