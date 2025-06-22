FROM python:3.12-slim
LABEL maintainer="magnetto54@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    adduser \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /files/media

RUN adduser --disabled-password --no-create-home my_user

RUN chown -R my_user /files/media
RUN chmod -R 755 /files/media

USER my_user
