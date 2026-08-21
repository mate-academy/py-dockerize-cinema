FROM python:3.10-alpine

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN apk add --no-cache libpq libjpeg zlib \
    && apk add --no-cache --virtual .build-deps \
        gcc musl-dev postgresql-dev jpeg-dev zlib-dev \
    && pip install --no-cache-dir -r requirements.txt \
    && apk del .build-deps \
    && adduser --disabled-password --no-create-home django-user \
    && mkdir -p /vol/web/media /vol/web/static \
    && chown -R django-user:django-user /vol/web

COPY --chown=django-user:django-user . .

USER django-user

