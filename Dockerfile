FROM python:3.12-alpine3.17
LABEL maintainer="lyaskov1@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Создаём директорию и пользователя
RUN mkdir -p /files/media \
 && adduser -D -H my_user \
 && chown -R my_user /files/media \
 && chmod -R 755 /files/media

USER my_user