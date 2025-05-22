FROM python:3.10.16-alpine3.20
LABEL maintainer="woops359@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN adduser
        --disabled-password\
        --home /home/django-user\
        django-user &&\
    mkdir -p /home/django-user &&Ї
    chown django-user:django-user /home/django-user

RUN mkdir -p /vol/web/media
RUN chown -R django-user /vol/
RUN chmod -R 755 /vol/web/


USER django-user
