FROM python:3.11.6-alpine3.18
LABEL maintainer="maksym.protsak@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR /cinema_service

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
