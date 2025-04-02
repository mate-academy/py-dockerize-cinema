FROM python:3.11.6-alpine3.18
LABEL maintainer="zkorvoz02@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /files/media

RUN adduser --disabled-password --no-create-home django-user && \
    chown -R django-user:django-user /files/media && \
    chmod -R 755 /files/media && \
    mkdir -p /vol/web/media

USER django-user
