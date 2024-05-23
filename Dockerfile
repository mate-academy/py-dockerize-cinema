FROM python:3.12-slim
LABEL maintainer="sma4no.7@gmail.com"

ENV PYTHOUNNBUFFERED 1

WORKDIR app/

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2


COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
RUN mkdir -p /files/media

RUN adduser \
        --disabled-password \
        --no-create-home \
        django-user

RUN chown -R django-user /files/media
RUN chmod -R 755 /files/media


USER django-user
