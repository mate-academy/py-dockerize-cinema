# Dockerfile
FROM python:3.11.6-alpine3.18

LABEL maintainer="Ohrimenko15@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
