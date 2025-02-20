FROM python:3.10-alpine3.13
LABEL authors="mindflux99@gmail.com"

ENV PYTHONUNBUFFERED=1

RUN apk update && apk add --no-cache dos2unix

WORKDIR /usr/src/requirements

COPY requirements.txt requirements.txt


RUN python -m pip install --upgrade pip && \
    pip install -r requirements.txt

WORKDIR /usr/src/app

COPY ./src .

COPY ./commands /usr/src/commands

RUN dos2unix /usr/src/commands/*.sh