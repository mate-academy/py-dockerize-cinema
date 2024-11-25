FROM python:3.9.16-alpine3.18
LABEL maintainer="szholudsd@gmail.com"

RUN apk update && apk add --no-cache \
    postgresql-dev gcc musl-dev python3-dev

ENV PYTHONUNBUFFERED=1
WORKDIR /app

COPY requirements.txt requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN mkdir -p /files/media

RUN adduser \
    --disabled-password \
    --no-create-home \
    my_user

RUN chown -R my_user /files/media
RUN chmod -R 755 /files/media


USER my_user
