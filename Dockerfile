FROM python:3.10.4-slim-buster
LABEL maintainer="anton.lasko1993@gmail.com"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

WORKDIR app/

COPY requirements.txt requirements.txt

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2 \
    && pip install drf-spectacular \
    && pip install djangorestframework-simplejwt

RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /vol/web/media

RUN adduser \
    --disabled-password \
    --no-create-home \
    django-user

RUN chown -R django-user:django-user /vol/
RUN chmod -R 755 /vol/web

USER django-user
