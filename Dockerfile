FROM python:3.11.6-alpine3.18

LABEL maintainer="mr.darmstadtium@gmail.com"

ENV PYTHOUNNBUFFERED 1

WORKDIR cinema/

COPY user .
COPY cinema .
COPY cinema_service .
COPY requirements.txt .

RUN pip isntall -r requirements.txt

COPY . .

RUN mkdir -p /files/media

RUN adduser \
    --disabled-password \
    --no-create-home \
    my_user

RUN chown -R my_user /files/media
RUN chmod -R 755 /files/media

USER my_user
