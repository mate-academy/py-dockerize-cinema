FROM python:alpine3.19
LABEL maintainer="max@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

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
