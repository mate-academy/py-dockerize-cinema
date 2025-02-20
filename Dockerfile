FROM python:3.10-alpine
LABEL authors="trukhanov.danya@gmail.com"

ENV PYTHONUNBUFFERED=1

RUN apk update && apk add --no-cache dos2unix

WORKDIR /usr/src/requirements

COPY requirements.txt requirements.txt

RUN python -m pip install --upgrade pip && pip install -r requirements.txt

WORKDIR /usr/src/app

RUN mkdir -p /usr/src/app/files/media

RUN adduser \
    --disabled-password \
    --no-create-home \
    my_user

RUN chown -R my_user /usr/src/app/files/media
RUN chmod -R 755 /usr/src/app/files/media

COPY ./src .

COPY ./commands /usr/src/commands

RUN dos2unix /usr/src/commands/*.sh

USER my_user
