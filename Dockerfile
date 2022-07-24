FROM python:3.10.4-alpine3.14
LABEL maintainer="example@example.com"

ENV PYTHONUNBUFERED 1

WORKDIR app/
# If used slim image: apt-get update && apt-get -y install libpq-dev gcc
# If pip update needed: RUN python -m pip install -U pip
RUN apk --no-cache add postgresql-client

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt && mkdir -p /vol/web/media

COPY . .

RUN adduser --disabled-password --no-create-home django-user && \
    chown -R django-user:django-user /vol/ && \
    chmod -R 755 /vol/web/

USER django-user
