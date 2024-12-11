FROM python:3.11-slim
LABEL maintainer="jacktyler2391@gmail.com"

ENV PYTHOUNNBUFFERED 1

WORKDIR /cinema

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .


RUN adduser \
        --disabled-password \
        --no-create-home \
        django-user
