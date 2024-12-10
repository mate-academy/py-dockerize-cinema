FROM python:3.10-slim-buster
LABEL maintainer="vladislav.tmf@gmail.com"

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

RUN adduser \
    --disabled-password \
    --no-create-home \
    django-user

RUN mkdir -p /app/media \
    && chown -R django-user:django-user /app \
    && chmod -R 755 /app/media

USER django-user
