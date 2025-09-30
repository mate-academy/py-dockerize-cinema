FROM python:3.11.6-alpine3.18
LABEL maintainer="zubritsky.misha@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app
RUN apk add --no-cache netcat-openbsd

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
COPY wait-for-db.sh /app/wait-for-db.sh
RUN chmod +x /app/wait-for-db.sh
RUN mkdir -p /files/media

RUN adduser \
        --disabled-password \
        --no-create-home \
        my_user

RUN chown -R my_user /files/media
RUN chmod -R 755 /files/media

USER my_user
