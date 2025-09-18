FROM python:3.13-alpine

ENV PYTHONOUNNBUFFERED=1
ENV PYTHONUNBUFFERED=1

WORKDIR /cinema

COPY requirements.txt .

RUN apk add --no-cache --virtual .build-deps \
      build-base \
      postgresql-dev \
      linux-headers \
      jpeg-dev \
      zlib-dev \
    && apk add --no-cache \
      postgresql-libs \
    && pip install --no-cache-dir -r requirements.txt \
    && apk del .build-deps

COPY . .

RUN mkdir -p /vol/web/static /vol/web/media \
    && adduser --disabled-password --no-create-home my_user \
    && chown -R my_user /vol \
    && chmod -R 755 /vol

USER my_user

EXPOSE 8000