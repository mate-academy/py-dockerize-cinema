FROM python:3.11.11-alpine3.21
LABEL maintainer="chorny.yura@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
