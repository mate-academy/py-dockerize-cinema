FROM python:3.11.6-alpine3.18
LABEL maintaner="dimasysoev20000@gmail.com"

ENV PYTHONBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /files/media

RUN adduser --disabled-password --no-create-home cinema_user \
    && chown -R cinema_user: /files/media
RUN chmod -R 755 /files/media

USER cinema_user
