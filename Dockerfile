FROM python:3.11.2-slim-buster
LABEL maintainer="eduardhabryd@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . .

RUN apt-get update \
    && apt-get -y install libpq-dev gcc

RUN pip install -r requirements.txt

RUN mkdir -p /vol/web/media/uploads/movies/ && chown -R 1000:1000 /vol

USER 1000
