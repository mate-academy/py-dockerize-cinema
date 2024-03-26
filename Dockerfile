FROM python:3.12-slim
LABEL maintainer="clarioruberia@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

RUN adduser \
         --disabled-password \
         --no-create-home \
         django-user
