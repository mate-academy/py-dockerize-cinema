FROM python:3.10-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .

RUN apk add --no-cache postgresql-client jpeg-dev
RUN apk add --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev musl-dev zlib-dev

RUN pip install --no-cache-dir -r requirements.txt

RUN apk del .tmp-build-deps

COPY . .

EXPOSE 8000

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static
RUN adduser \
    --disabled-password \
    --no-create-home \
    django-user

RUN chown -R django-user:django-user /vol/
RUN chmod -R 755 /vol/web

USER django-user
