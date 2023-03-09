FROM python:3.11.0-alpine

LABEL maintainer="terrya@ukr.net"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN adduser \
        --disabled-password \
        --no-create-home \
        django-user

RUN chown -R django-user:user /vol/
    chmod -R 755 /vol/web/

USER django-user
