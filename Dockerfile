FROM python:3.11-alpine3.18

LABEL maintainer="zahrebelnyivadym@gmail.com"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

RUN mkdir -p /vol/web/media /vol/web/static && \
    adduser --disabled-password --no-create-home django-user && \
    chown -R django-user:django-user /vol/ && \
    chmod -R 755 /vol/

USER django-user