FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    HOME=/home/django-user

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential libpq-dev libjpeg-dev zlib1g-dev libpng-dev curl \
 && rm -rf /var/lib/apt/lists/*

RUN adduser --disabled-password --gecos "" --home /home/django-user django-user

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /vol/web/media /vol/web/static \
 && chown -R django-user:django-user /vol /app \
 && chmod -R 755 /vol/web

USER django-user
EXPOSE 8000
