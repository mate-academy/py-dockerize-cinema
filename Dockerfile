FROM python:3.11-alpine
LABEL maintainer="volokitin.vitaliy@icloud.com"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

RUN apk add --no-cache gcc musl-dev postgresql-dev zlib-dev jpeg-dev

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN mkdir -p /files/media /app/staticfiles \
    && adduser -D my_user \
    && chown -R my_user:my_user /files/media /app/staticfiles \
    && chmod -R 755 /files/media /app/staticfiles

USER my_user
