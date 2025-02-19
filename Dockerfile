FROM python:3.11.11-alpine3.19
LABEL maintainer="imtence@gmail.com"

ENV PYTHONBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
RUN mkdir -p /files/media

RUN adduser \
    --disabled-password \
    --no-create-home \
    django-user

RUN chown -R django-user /files/media
RUN chmod -R 755 /files/media

USER django-user
