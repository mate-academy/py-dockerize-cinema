FROM python:3.12-slim
LABEL maintainer="super.racing@urk.net"

ENV PYTHOUNNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN adduser \
        --disabled-password \
        --shell "/sbin/nologin" \
        --no-create-home \
        django-user

USER django-user

COPY . .
