FROM python:3.12-alpine3.18
LABEL maintainer="lauman@ukr.net"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /files/media && \
    chown -R my_user /files/media && \
    chmod -R 755 /files/media

RUN adduser --disabled-password --no-create-home my_user

USER my_user
