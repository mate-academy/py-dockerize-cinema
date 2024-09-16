FROM python:3.10-slim-buster
LABEL maintainer="busterakel@gmail.com"

ENV PYTHONBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /files/media/

RUN adduser \
    --disabled-password \
    --no-create-home \
    django-user

RUN chown -R django-user:django-user /files/media/
RUN chmod -R 755 /files/media/

USER django-user
