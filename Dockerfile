FROM python:3.11-slim-buster

LABEL authors="sfink417865@gmail.com"

ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt requirements.txt
RUN apt-get update && apt-get install -y postgresql-client libjpeg-dev
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc libc6-dev libpq-dev musl-dev zlib1g zlib1g-dev \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*
RUN pip install -r requirements.txt
COPY . .
RUN mkdir -p /vol/web/media
RUN adduser \
    --disabled-password \
    --no-create-home \
    django-user
RUN chown -R django-user:django-user /vol/
RUN chmod -R 755 /vol/web
USER django-user
