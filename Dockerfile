FROM python:3.11-slim-buster
LABEL maintainer="Max Katkalov <maxkatkalov@gmail.com>"

ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

WORKDIR /app

COPY . .

RUN adduser \
    --disabled-password \
    --no-create-home \
    django-user

USER django-user
