FROM python:3.11-alpine

LABEL maintainer="verbikyullya@gmail.com"

ENV  PYTHONUNBUFFERED 1

WORKDIR app/

# Install system dependencies
RUN apk add --no-cache zlib-dev

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /vol/web/media

RUN adduser \
    --disabled-password \
    --no-create-home \
    django-user

RUN chown -R django-user:django-user /vol/
RUN chmod -R 755 /vol/web/

USER django-user
