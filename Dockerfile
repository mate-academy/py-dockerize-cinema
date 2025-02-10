FROM python:3.11-alpine3.21

WORKDIR /app

COPY requirements.txt /app/

# Устанавливаем системные зависимости
RUN apk update && apk add --no-cache \
    gcc \
    musl-dev \
    postgresql-dev \
    zlib-dev \
    jpeg-dev \
    libpng-dev \
    python3-dev \
    py3-pip \
    && pip install --upgrade pip setuptools wheel

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install psycopg2-binary


COPY . /app/

