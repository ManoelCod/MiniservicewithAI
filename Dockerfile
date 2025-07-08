# Usa imagem oficial do Python
FROM python:3.11-slim

# Define diretório de trabalho
WORKDIR /app

# Copia todos os arquivos do projeto
COPY . .

# Instala dependências
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Expõe a porta do Flask (ajuste se usar outra)
EXPOSE 5000

# Comando padrão: inicia a aplicação via run.py
CMD ["python", "run.py"]