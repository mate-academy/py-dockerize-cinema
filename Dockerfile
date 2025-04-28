FROM python:3.11-alpine

LABEL maintainer="kotnazarr2005@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .
RUN mkdir -p /vol/web/media



RUN adduser \
        --disabled-password \
        --no-create-home\
        django-user

RUN chown -R django-user:django-user /vol/web/media
RUN chmod -R 755 /vol/web/media

USER django-user