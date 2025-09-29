FROM python:3.10.8-slim

LABEL maintainer="lyubinska"

ENV PYTHONUNBUFFERED 1

WORKDIR /cinema

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt
COPY . .

RUN mkdir -p /files/media
RUN mkdir -p /files/static

RUN adduser \
    --disabled-password \
    --no-create-home \
    my_user

RUN chown -R my_user /files/media
RUN chmod -R 755 /files/media

USER my_user
