FROM python:3.12.0-alpine3.18

LABEL maintainer="slradbez@gmail.com"

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN mkdir -p /files/media

RUN adduser \
    --disabled-password \
    --no-create-home \
    my_user

RUN chmod -R my_user /files/media
RUN chmod -R 755 /files/media

USER my_user
