FROM python:3.10-alpine

LABEL maintainer="Artem Yur"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /tmp/requirements.txt

RUN apk add --no-cache \
        libpq \
        libjpeg-turbo \
        zlib \
    && apk add --no-cache --virtual .build-deps \
        gcc \
        musl-dev \
        postgresql-dev \
        libjpeg-turbo-dev \
        zlib-dev \
        linux-headers \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r /tmp/requirements.txt \
    && apk del .build-deps \
    && rm -f /tmp/requirements.txt

COPY . /app

RUN mkdir -p /vol/web/media \
    && mkdir -p /vol/web/static \
    && adduser \
        --disabled-password \
        --no-create-home \
        django-user \
    && chown -R django-user:django-user /vol \
    && chmod -R 755 /vol

USER django-user

EXPOSE 8000
