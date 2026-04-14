FROM python:3.13-slim

LABEL maintainer="Marek Drządzewski"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

RUN adduser \
    --disabled-password \
    --no-create-home \
    django-user

RUN mkdir -p /vol/web \
    && chown -R django-user:django-user /vol \
    && chmod -R 755 /vol/web

USER django-user