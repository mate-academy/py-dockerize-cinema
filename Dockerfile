FROM python:3.10-alpine
LABEL maintainer="serhiibhryniuk@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt

RUN apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev && \
    pip install -r requirements.txt && \
    apk del .tmp-build-deps

COPY . .

RUN mkdir -p /vol/web/media && \
    mkdir -p /vol/web/static && \
    adduser -D django-user && \
    chown -R django-user:django-user /vol && \
    chmod -R 755 /vol

USER django-user