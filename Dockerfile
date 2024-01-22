FROM python:3.12.0-slim

LABEL maintainer ="nsd7night@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt


COPY . .
