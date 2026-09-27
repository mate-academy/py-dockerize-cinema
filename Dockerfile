FROM python:3.10-alpine3.18
LABEL maintainer="you@example.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt

RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
        gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
RUN pip install --no-cache-dir -r requirements.txt
RUN apk del .tmp-build-deps

COPY . .

RUN mkdir -p /app/media

RUN adduser --disabled-password --no-create-home django-user
RUN chown -R django-user /app/media
RUN chmod -R 755 /app/media

USER django-user

EXPOSE 8000
