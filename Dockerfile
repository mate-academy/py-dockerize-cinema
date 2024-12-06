FROM python:3.10-alpine3.20
LABEL authors="p4niQ"

ENV PYTHONUNBUFFERED 1

WORKDIR /app

ENV PYTHONPATH=${PYTHONPATH}:/app/management/commands

RUN apk add --no-cache \
    build-base \
    jpeg-dev \
    zlib-dev \
    libjpeg \
    gcc \
    musl-dev \
    postgresql-dev

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .
