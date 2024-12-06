FROM python:3.10.5-slim-buster
LABEL maintainer="ansmbox@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN apt-get update && apt-get -y install libpq-dev gcc netcat
RUN pip install -r requirements.txt

COPY . .

RUN adduser \
    --disabled-password \
    --no-create-home \
    django-user

RUN mkdir -p /var/web/media
RUN chown -R django-user:django-user /var/web/media
RUN chmod -R 755 /var/web

USER django-user
