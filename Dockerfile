FROM python:3.12-slim

LABEL author="Marek Biela"

ENV PYTHONBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN adduser \
        --disabled-password \
        --no-create-home \
        django-user

RUN mkdir -p /app/media/uploads && \
    chown -R django-user:django-user /app/media

USER django-user