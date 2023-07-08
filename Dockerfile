FROM python:3.10.4-slim-buster
LABEL authors="sebshe3@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

ADD . .
RUN pip install --no-cache-dir -r requirements.txt && \
    adduser --disabled-password --no-create-home django-user

USER django-user
