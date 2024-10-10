FROM python:3.12.7-alpine3.20
LABEL maintainer="a.g.e.n.t.4282@gmail.com"

ENV PYTHONBUFFERED 1

WORKDIR app/

RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /files/media

RUN adduser --disabled-password --no-create-home admin

RUN chown -R admin /files/media
RUN chmod -R 755 /files/media

USER admin