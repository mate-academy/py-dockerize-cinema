FROM python:3.10.21-slim

LABEL maintainer="olykhorovych@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

RUN adduser \
    --disabled-password \
    --no-create-home \
    django-user && \
    mkdir -p /var/www/media /var/www/static && \
    chown -R  django-user:django-user /var/www && \
    chmod -R 755 /var/www

COPY --chown=django-user:django-user . /app

RUN chmod -R 755 /app

USER django-user
