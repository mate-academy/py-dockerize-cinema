FROM python:3.12.2-alpine3.19
LABEL maintainer="sanyok.it@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /files/media

RUN adduser \
    --disabled-password \
    --no-create-home \
    admin

RUN chown -R admin /files/media
RUN chmod -R 755 /files/media

EXPOSE 8000

USER admin

