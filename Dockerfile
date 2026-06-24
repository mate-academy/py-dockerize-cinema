FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN mkdir -p /files/media /files/static

RUN adduser \
        --disabled-password \
        --no-create-home \
        django-user

RUN chown -R django-user /files
RUN chmod -R 755 /files

USER django-user
