FROM python:3.11.0-alpine

LABEL maintainer="terrya@ukr.net"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
