FROM python:3.13.13-alpine3.23
LABEL maintainer="vovakucin082@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /app/files/media
