FROM python:3.11.0-slim-buster
LABEL maintainer="roffi37"

ENV PYTHONBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /vol/web/media

RUN adduser \
    --disabled-password \
    --no-create-home \
    django-user

RUN chown -r django-user:django-user /vol/
RUN chmod -r 755 /vol/web/

RUN apk add --no-cache bash

USER django-user