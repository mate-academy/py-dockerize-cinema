FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apk add --update --no-cache postgresql-client jpeg-dev \
    && apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev zlib zlib-dev

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt \
    && apk del .tmp-build-deps

COPY . /app/

RUN mkdir -p /vol/web/media \
    && mkdir -p /vol/web/static \
    && adduser -D django-user \
    && chown -R django-user:django-user /vol/ \
    && chown -R django-user:django-user /app/ \
    && chmod -R 755 /vol

USER django-user
