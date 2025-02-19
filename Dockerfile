FROM python:3.13-alpine

WORKDIR /usr/src/app/

# psycopg build dependencies: C compiler, headers
RUN apk update && apk add --no-cache --virtual .build-deps python3-dev gcc libc-dev

RUN apk add --no-cache libpq-dev

WORKDIR /usr/src/app/

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# clean up build dependencies
RUN apk del .build-deps && rm -rf /var/cache/apk/*

COPY . .

RUN adduser --disabled-password --no-create-home django-user

RUN mkdir -p /usr/src/app/media/uploads/ \
    && chown -R django-user:django-user /usr/src/app/media/ \
    && chmod -R 755 /usr/src/app/media/

USER django-user
