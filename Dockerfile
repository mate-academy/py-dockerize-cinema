FROM python:3.10.12-slim-buster
LABEL maintainer="andy77andy77andy@gmail.com"

ENV PYTHONUNBUFFERED 1
WORKDIR app/

#RUN apt-get update\
#    && apt-get -y install libpq-dev gcc
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN adduser \
        --disabled-password \
        --no-create-home \
        django-user

USER django-user
