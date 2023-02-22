FROM python:3.10.6-slim-buster
LABEL maintainer="chumak7377@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .
