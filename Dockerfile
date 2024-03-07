FROM python:3.10.4-slim-buster

LABEL maintainer=kravetsbodj@gmail.com

ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt

RUN apt-get update \
    && apt-get -y install libpq-dev gcc

RUN pip install -r requirements.txt

WORKDIR /app

COPY . .

RUN adduser \
        --disabled-password \
        --no-create-home \
        django-user

USER django-user
