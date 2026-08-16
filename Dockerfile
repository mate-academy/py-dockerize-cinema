FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN adduser \
    --disabled-password \
    --no-create-home \
    django-user

RUN mkdir -p /vol/web/media \
    && mkdir -p /vol/web/static \
    && chown -R django-user:django-user /vol \
    && chmod -R 755 /vol/web

COPY . .

USER django-user