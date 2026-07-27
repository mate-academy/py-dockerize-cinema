FROM python:3.11-slim

LABEL maintainer="seu_nome"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

RUN mkdir -p /vol/web/media && \
    mkdir -p /vol/web/static

RUN useradd -m appuser && \
    chown -R appuser:appuser /app /vol && \
    chmod -R 755 /vol
USER appuser

EXPOSE 8000
