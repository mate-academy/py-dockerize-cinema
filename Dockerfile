FROM python:3.13-slim
LABEL authors="devjohny"

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt  --no-cache-dir

COPY . .

RUN mkdir -p /files/media

RUN adduser \
        --disabled-password \
        --no-create-home \
        my_user

RUN chown -R my_user /files/media && chmod -R 755 /files/media

USER my_user