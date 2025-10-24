FROM python:3.12-alpine3.22

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt requirements.txt

RUN apk add --no-cache gcc musl-dev postgresql-dev postgresql-libs
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p /files/media

RUN adduser \
        --disabled-password \
        --no-create-home \
        my-user

RUN chown -R my-user /files/media
RUN chmod -R 755 /files/media

USER my-user
COPY . .