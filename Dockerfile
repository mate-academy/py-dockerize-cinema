FROM python:3.11.8-alpine3.18
LABEL maintainer="ivchenkomykhailo@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
RUN mkdir -p /files/media

RUN adduser \
    --disabled-password \
    --no-create-home \
    app_user

RUN chown -R app_user /files/media
RUN chmod -R 755 /files/media

USER app_user
