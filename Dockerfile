FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /requirements.txt

RUN apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-build-deps \
        gcc libc-dev linux-headers postgresql-dev && \
    pip install -r /requirements.txt && \
    apk del .tmp-build-deps

COPY . /app

RUN mkdir -p /vol/web/media && \
    mkdir -p /vol/web/static && \
    adduser -D user && \
    chown -R user:user /vol && \
    chmod -R 755 /vol

USER user
