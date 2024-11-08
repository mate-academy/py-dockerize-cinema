FROM python:3.11.6-alpine3.18
LABEL maintainer="mishchuk.anastasiia@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

RUN apk add -u zlib-dev jpeg-dev gcc musl-dev

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
RUN mkdir -p /files/media

RUN adduser \
    --disabled-password \
    --no-create-home \
    my_user

RUN chown -R my_user:my_user /files/media
RUN chmod -R 755 /files/media

USER my_user
