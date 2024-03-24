FROM python:3.9-slim

LABEL maintainer="a.shpakovych.work@gmail.com"

ENV PYTHONBUFFERED 1

WORKDIR /app

COPY requirements.txt requirements.txt

RUN apt-get update && apt-get install -y --no-install-recommends libpq-dev gcc

RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /vol/web/media

RUN adduser \
         --disabled-password \
         --no-create-home\
         django-user

RUN chown -R django-user:django-user /vol/

RUN chown -R 755 /vol/web/

USER django-user
