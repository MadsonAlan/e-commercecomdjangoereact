# Usa imagem oficial do Python
FROM python:3.11-slim

# Define o diretório de trabalho no container
WORKDIR /code

# Instala dependências do sistema (ex: libpq para PostgreSQL)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

RUN apt-get update && \
    apt-get install -y postgresql-client && \
    apt-get clean

# Copia o requirements.txt (se existir)
COPY requirements.txt .

# Instala as dependências Python
RUN pip install --upgrade pip && pip install -r requirements.txt django djangorestframework django-cors-headers djangorestframework-simplejwt Pillow whitenoise psycopg2-binary


# Copia o restante do projeto para o container
COPY . .
RUN chmod +x wait-for-it.sh

# Expõe a porta 8000 (opcional – apenas documenta)
EXPOSE 8000

CMD [ "./wait-for-it.sh ${DB_HOST}:${DB_PORT}" ]