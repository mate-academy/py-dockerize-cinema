FROM python:3.11.6-alpine3.18
LABEL maintainer="zedxi236@ukr.net"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt && \
    adduser --disabled-password --no-create-home django-user

COPY . .
RUN mkdir -p /vol/web/media && \
    mkdir -p /vol/web/static && \
    chown -R django-user:django-user /vol/ && \
    chmod -R 755 /vol/web/

USER django-user
