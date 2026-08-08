FROM python:3.10-alpine3.18

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN apk add --update --no-cache postgresql-client jpeg-dev \
    && apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev zlib zlib-dev linux-headers \
    && pip install --no-cache-dir -r requirements.txt \
    && apk del .tmp-build-deps

COPY . .

RUN mkdir -p /vol/web/media /vol/web/static

RUN adduser --disabled-password --no-create-home django-user \
    && chown -R django-user:django-user /vol \
    && chmod -R 755 /vol/web

USER django-user
