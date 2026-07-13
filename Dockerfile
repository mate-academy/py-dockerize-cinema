FROM python:3.11-alpine
LABEL maintainer="wachax52"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt

RUN apk add --update --no-cache postgresql-client jpeg-dev \
    && apk add --update --no-cache --virtual .tmp-build-deps \
        gcc libc-dev linux-headers postgresql-dev zlib zlib-dev \
    && pip install --no-cache-dir -r requirements.txt \
    && apk del .tmp-build-deps

COPY . .

RUN mkdir -p /files/media /files/static

RUN adduser --disabled-password --no-create-home django-user \
    && chown -R django-user:django-user /files \
    && chmod -R 755 /files

USER django-user
