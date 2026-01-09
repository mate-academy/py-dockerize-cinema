FROM python:3.10-alpine
LABEL maintainer="your_email@example.com"

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./requirements.txt /tmp/requirements.txt

RUN apk add --no-cache postgresql-client jpeg-dev && \
    apk add --no-cache --virtual .build-deps \
        gcc python3-dev musl-dev postgresql-dev zlib-dev && \
    pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    apk del .build-deps

COPY . .

RUN adduser \
        --disabled-password \
        --no-create-home \
        django-user && \
    mkdir -p /app/media /app/static && \
    chown -R django-user:django-user /app && \
    chmod -R 755 /app && \
    find /app -type f -exec chmod 644 {} +

USER django-user
