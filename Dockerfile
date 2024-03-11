FROM python:3.12-slim

ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt /requirements.txt

RUN apt-get update && \
    apt-get install -y zlib1g-dev libjpeg-dev gcc musl-dev

RUN pip install -r requirements.txt

RUN adduser \
        --disabled-password \
        --no-create-home \
        django-user

USER django-user

WORKDIR /app

COPY . .
