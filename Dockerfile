FROM python:3.10.8-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /vol/web/media /vol/web/static && \
    chmod -R 755 /vol/web && \
    useradd -m appuser && \
    chown -R appuser:appuser /app

USER appuser
