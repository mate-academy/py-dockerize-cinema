FROM python:3.10.17-alpine3.21
LABEL maintainer="akolomiec982@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /files/media

RUN apk add --no-cache bash

RUN adduser \
    --disabled-password \
    --no-create-home \
    admin_user

RUN chown -R admin_user /files/media
RUN chmod -R 755 /files/media

USER admin_user