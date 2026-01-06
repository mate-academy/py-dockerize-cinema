FROM python:3.13-alpine
LABEL maintainer="brebston7@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
RUN mkdir -p /files/media

RUN adduser \
    --disabled-password \
    --no-create-home \
    brebston

RUN chown -R brebston /files/media
RUN chmod -R 755 /files/media

USER brebston