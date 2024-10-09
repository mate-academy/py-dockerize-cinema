FROM python:3.12.5-alpine3.20
LABEL maintainer="Sergio0bbb"

WORKDIR /usr/src/app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PIP_NO_CACHE_DIR off

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
