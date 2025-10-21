FROM python:3.13-slim

LABEL authors="Skrev"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    gcc \
    && apt-get clean

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . .
RUN mkdir -p /files/media /files/static

RUN adduser \
    --disabled-password \
    --no-create-home \
    my_user

RUN chown -R my_user:my_user app/files
RUN chmod -R 755 app/files

USER my_user
