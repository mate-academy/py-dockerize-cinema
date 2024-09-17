FROM python:3.10.0-slim-buster

LABEL maintainer="leetwinoff92@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /vol/web/media

RUN adduser \
    --disabled-password \
    --no-create-home \
    django-user

RUN chown -R django-user:django-user /vol/
RUN chmod -R 755 /vol/web/
RUN chmod -R 777 /vol/web/media/

USER django-user
