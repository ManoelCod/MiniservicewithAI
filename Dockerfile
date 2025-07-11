# Usa imagem oficial do Python
FROM python:3.11-slim

# Instala o supervisor
RUN apt-get update && apt-get install -y supervisor

# Define diretório de trabalho
WORKDIR /app

# Copia tudo
COPY . .

# Instala dependências do Python
RUN pip install --upgrade pip && \
    pip install -r requirements.txt
    

# Copia config do supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Expõe a porta do Flask
EXPOSE 5000

# Executa supervisor para iniciar os dois serviços
CMD ["supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]