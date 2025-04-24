FROM python:3.13
LABEL maintainer="wenhun1@gmail.com"

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR app

RUN apt-get update && apt-get install -y libpq-dev gcc python3-dev

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /files/media

RUN adduser \
    --disabled-password \
    --no-create-home \
    my_user

RUN chown -R my_user /files/media
RUN chmod -R 755 /files/media

USER my_user
