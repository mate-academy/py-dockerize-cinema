FROM python:3.12-alpine

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN apk add --no-cache postgresql-client && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

RUN adduser --disabled-password --no-create-home app_user && \
    mkdir -p /vol/web/media /vol/web/static && \
    chown -R app_user:app_user /vol/web

USER app_user

EXPOSE 8000