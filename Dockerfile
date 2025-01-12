FROM python:3.8.10-alpine

LABEL authors="frezworx"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt

RUN  pip install --no-cache-dir -r requirements.txt

COPY . .
RUN mkdir -p /files/media

RUN adduser --disabled-password --no-create-home my-user

RUN chown -R my-user /files/media
RUN chmod -R 755 /files/media
USER my-user