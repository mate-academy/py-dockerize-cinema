FROM python:3.7.5-slim-buster
LABEL maintainer="maksym71417@gmail.com"

ENV PYTHONBUFFERED 1

WORKDIR cinema_app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /vol/web/media

RUN apt-get update \
    && apt-get -y install libpq-dev gcc

RUN adduser \
    --disabled-password \
    --no-create-home \
    django-user

RUN chown -R django-user:django-user /vol/
RUN chmod -R 755 /vol/web/

USER django-user
