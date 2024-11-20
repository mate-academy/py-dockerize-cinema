FROM python:3.11.6-alpine3.18
LABEL maintainer="arsen.test.mess@gmail.com"

RUN apk add --no-cache \
    zlib-dev \
    jpeg-dev \
    gcc \
    musl-dev \
    libjpeg \
    libffi-dev \
    make

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .
