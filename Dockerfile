# stage 1: psycopg build dependencies
FROM python:3.13-alpine AS builder

# psycopg needs C compiler, headers
RUN apk update && \
    apk add --no-cache --virtual .build-deps python3-dev gcc libc-dev libpq-dev

WORKDIR /usr/src/app/

COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

FROM python:3.13-alpine

# runtime dep of psycopg
RUN apk update && \
    apk add --no-cache libpq

WORKDIR /usr/src/app/

# copy installed packages from builder stage
COPY --from=builder /usr/local/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages
COPY --from=builder /usr/src/app /usr/src/app

RUN adduser --disabled-password --no-create-home django-user

RUN mkdir -p /usr/src/app/media/uploads/ \
    && chown -R django-user:django-user /usr/src/app/media/ \
    && chmod -R 755 /usr/src/app/media/

USER django-user
