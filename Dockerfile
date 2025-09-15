FROM python:3.11.13-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN mkdir -p /vol/web/media

RUN adduser \
        --disabled-password \
        --no-create-home \
        django-user

RUN chown -R django-user /vol/web/media
RUN chmod -R 755 /vol/web/media

USER django-user
