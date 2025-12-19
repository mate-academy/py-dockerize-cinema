FROM python:3.11-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./requirements.txt .

RUN apk add --no-cache postgresql-client && \
    apk add --no-cache --virtual .tmp-deps build-base postgresql-dev musl-dev && \
    pip install --no-cache-dir -r requirements.txt && \
    apk del .tmp-deps && \
    adduser --disabled-password --no-create-home django-user && \
    mkdir -p /vol/web/media && \
    mkdir -p /vol/web/static && \
    chown -R django-user:django-user /vol && \
    chmod -R 755 /vol

COPY . .

USER django-user