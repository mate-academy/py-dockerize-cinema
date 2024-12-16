FROM python:3.11.6-alpine3.18
LABEL maintainer="lev2099@gmail.com"

ENV PYTHONNBUFFERED 1

WORKDIR /cinema_service


COPY requirements.txt /cinema_service

RUN pip install --no-cache-dir -r requirements.txt

COPY . /cinema_service