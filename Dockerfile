FROM python:3.11-slim

WORKDIR /app

ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

RUN adduser \
    --disabled-password \
    --no-create-home \
    django-user

RUN mkdir -p /vol/web/media

RUN chown -R django-user:django-user /vol/
RUN chown -R 755 /vol/web/

USER django-user
