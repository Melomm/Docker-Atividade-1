# Imagem base oficial do Python
FROM python:3.11-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo de dependências
COPY requirements.txt .

# Instala o framework Flask
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código fonte da aplicação para o container
COPY app.py .
COPY templates/ templates/

# Expõe a porta 80
EXPOSE 80

# Define o comando para iniciar a aplicação
CMD ["python", "app.py"]