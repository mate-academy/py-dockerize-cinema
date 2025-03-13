FROM python:3.10.16-alpine3.20
LABEL maintainer="nikolajtarasenko71@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN adduser \
        --disabled-password \
        --no-create-home \
        django-user
