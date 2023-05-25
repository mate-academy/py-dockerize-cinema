FROM python:3.11-alpine
LABEL authors="lotrikys@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

ADD . .
RUN pip install --no-cache-dir -r requirements.txt && \
    adduser --disabled-password --no-create-home django-user

USER django-user
