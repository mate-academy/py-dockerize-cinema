FROM python:3.11.6-alpine3.18
LABEL authors="Fedot0v"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /files/media

RUN mkdir -p /files/media && \
    adduser --disabled-password --no-create-home my_user && \
    chown -R my_user /files/media && \
    chmod -R 755 /files/media

USER my_user
