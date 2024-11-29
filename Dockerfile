FROM python:3.10-slim

LABEL maintainer="v.s.viesich@gmail.com"

ENV PYTHOUNNBUFFERED=1
WORKDIR /app/

COPY requirements.txt requirements.txt

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && apt-get clean

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN adduser \
    --disabled-password \
    --no-create-home \
    my_user

RUN mkdir -p /files/media /app/files \
    && chown -R my_user /files/media /app/files \
    && chmod -R 755 /files/media /app/files

USER my_user
