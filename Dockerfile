FROM python:3.11.6-alpine3.18
LABEL maintainer="kenedy11@ukr.net"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /files/media \
    && adduser -D -H my_user \
    && chown -R my_user /files/media \
    && chmod -R 755 /files/media

USER my_user
