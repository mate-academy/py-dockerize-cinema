FROM python:3.11.6-alpine3.18

LABEL maintainer="malovaniy.an@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt

COPY . .

RUN pip install -r requirements.txt

RUN mkdir -p /files/media

RUN adduser \
    --disabled-password \
    --no-create-home \
    common_user

RUN chown -R common_user /files/media

RUN chmod -R 755 /files/media

USER common_user
