FROM python:3.11.6-alpine3.18
LABEL maintainer="shevchukkdmytro@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app


RUN apk add --no-cache postgresql-libs

RUN apk add --no-cache --virtual .build-deps \
    build-base \
    postgresql-dev \
    gcc \
    musl-dev \
    linux-headers \
    libffi-dev \
    zlib-dev \
    jpeg-dev

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

RUN apk del .build-deps

COPY . .

RUN addgroup -S app && adduser -S -G app my_user

RUN mkdir -p /files/media /files/static \
    && chown -R my_user:app /app /files \
    && chmod -R 755 /files

USER my_user

EXPOSE 8000