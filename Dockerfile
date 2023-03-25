FROM python:3.9.6-alpine

LABEL maintainer="bythewaters800@gmail.com"
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN mkdir -p /vol/web/media

RUN adduser \
    --disabled-password \
    --no-create-home \
    django-user

RUN chown -R django-user:django-user /vol/
RUN chmod -R 755 /vol/web/

USER django-user
