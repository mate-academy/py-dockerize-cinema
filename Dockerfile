FROM python:3.11.6-alpine3.18
LABEL maintainer="ilyakhomutov613@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /files/media

RUN adduser \
    --disabled-password \
    my_user

RUN chown -R my_user /files/media
RUN chmod -R 755 /files/media

USER my_user
