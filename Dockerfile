FROM python:3.13.6-alpine3.21

LABEL maintainer="aav162807@gmail.com"

WORKDIR app/

RUN apk add --no-cache gcc musl-dev postgresql-dev libpq-dev

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /files/media /files/static

RUN adduser -D -H my_user

RUN chown -R my_user /files/media /files/static
RUN chmod -R 755 /files/media /files/static

USER my_user
