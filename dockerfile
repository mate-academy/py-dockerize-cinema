FROM python:3.11-alpine

WORKDIR /app

COPY requirements.txt .

RUN apk add --update --no-cache postgresql-client jpeg libjpeg \
    && apk add --update --no-cache --virtual .tmp-build-deps \
       gcc libc-dev postgresql-dev musl-dev zlib-dev jpeg-dev \
    && pip install --no-cache-dir -r requirements.txt \
    && apk del .tmp-build-deps

RUN mkdir -p /vol/web/media /vol/web/static

RUN adduser \
    --disabled-password \
    --no-create-home \
    django-user

RUN chown -R django-user:django-user /vol/

RUN chmod -R 755 /vol/web/

USER django-user

COPY . .

EXPOSE 8000
