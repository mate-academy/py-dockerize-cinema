FROM python:3.11-alpine

LABEL maintainer="cinema-service"

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN apk add --no-cache \
    postgresql-client \
    jpeg-dev \
    && apk add --no-cache --virtual .build-deps \
    gcc \
    musl-dev \
    postgresql-dev \
    zlib-dev \
    libjpeg

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
    && apk del .build-deps

COPY . .

RUN mkdir -p /vol/web/media /vol/web/static \
    && adduser --disabled-password --no-create-home app_user \
    && chown -R app_user:app_user /vol \
    && chmod -R 755 /vol

USER app_user
