FROM python:3.9.2-slim-buster
LABEL maintainer="yaroslavmazurkevych@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR cinema/

COPY requirements.txt requirements.txt

RUN apt-get update && apt-get -y install libpq-dev gcc

RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /vol/web/media

RUN adduser \
    --disabled-password \
    --no-create-home \
    django-user

RUN chown -R django-user:django-user /vol/

USER django-user
