FROM python:3.13.7-alpine3.21

ENV PYTHONUNBUFFERED=1

RUN apk add --no-cache bash

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
RUN mkdir -p /vol/web/media

RUN adduser \
        --disabled-password \
        --no-create-home \
        django-user

RUN chown -R django-user /vol/web/media
RUN chmod -R 755 /vol/web/media

USER django-user
