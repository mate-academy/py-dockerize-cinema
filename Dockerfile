FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    libpq-dev gcc musl-dev libjpeg-dev zlib1g-dev \
    && rm -rf /var/lib/apt/lists/*

RUN adduser \
    --disabled-password \
    --no-create-home \
    django-user

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /vol/web/media && \
    mkdir -p /vol/web/static && \
    chown -R django-user:django-user /vol && \
    chmod -R 755 /vol/web

USER django-user
