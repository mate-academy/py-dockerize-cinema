FROM python:3.12-slim

LABEL maintainer="sserebri@gmail.com"

WORKDIR /app/

ENV PYTHONUNBUFFERED=1

EXPOSE 8000

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt && \
    mkdir -p "/files/media/" && \
    adduser --disabled-password --no-create-home django-user --gecos "" && \
    chown -R django-user:django-user "/files/media/" && \
    chmod -R 755 "/files/media"

USER django-user

COPY . .
