FROM python:3.12.2-alpine3.19
LABEL maintainer="rusipbox@gmail.com"

ENV PYTHOUNNBUFFERED 1

WORKDIR cinema/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
RUN mkdir -p /files/media

RUN adduser \
         --disabled-password \
         --no-create-home \
         baranovr-user

RUN chown -R baranovr-user:baranovr-user /files/
RUN chmod -R 755 /files/

USER baranovr-user
