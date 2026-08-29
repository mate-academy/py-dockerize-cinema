FROM python:3.11-alpine
LABEL maintainer="your_name"

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

RUN apk add --no-cache \
    gcc \
    musl-dev \
    postgresql-dev \
    jpeg-dev \
    zlib-dev \
    libffi-dev

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

RUN mkdir -p /vol/web/media /vol/web/static && \
    mkdir -p /app/media /app/static && \
    adduser -D -H django-user && \
    chown -R django-user:django-user /app /vol/ && \
    chmod -R 755 /app /vol/

USER django-user