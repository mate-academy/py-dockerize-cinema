FROM python:3.11.6-alpine3.18

ENV PYTHONUNBUFFERED 1

RUN apk add --no-cache \
    libjpeg-turbo-dev \
    zlib-dev \
    freetype-dev \
    lcms2-dev \
    openjpeg-dev \
    tiff-dev \
    harfbuzz-dev \
    fribidi-dev

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /files/media

RUN adduser \
    --disabled-password \
    --no-create-home \
    my_user

RUN chown -R my_user /files/media
RUN chmod -R 755 /files/media

USER my_user
