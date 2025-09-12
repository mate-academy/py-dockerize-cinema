FROM python:3.12-alpine3.22

LABEL maintainer="serhiibasok@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt


RUN apk add --no-cache postgresql-client

COPY . .

RUN mkdir -p /files/media

RUN adduser -D -H django-user

RUN chown -R django-user /files/media && \
    chmod -R 755 /files/media


USER django-user