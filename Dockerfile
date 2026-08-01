FROM python:3.10.8-slim

LABEL maintainer="sabina.gamidova.dev@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt \
    && adduser --disabled-password --no-create-home appuser \
    && mkdir -p /files/media /files/static \
    && chown -R appuser:appuser /files \
    && chmod -R 755 /files

COPY . .

USER appuser
