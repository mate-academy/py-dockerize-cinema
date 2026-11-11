FROM python:3.14-alpine

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt

RUN apk add --update --no-cache postgresql-client jpeg-dev && \
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev zlib zlib-dev && \
    pip install --upgrade pip && \
    pip install -r requirements.txt && \
    apk del .tmp-build-deps

COPY . .

RUN mkdir -p /vol/web/media && \
    mkdir -p /vol/web/static && \
    adduser -D user && \
    chown -R user:user /vol && \
    chmod -R 755 /vol

USER user
