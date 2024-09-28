FROM python:3.11-alpine
LABEL mainteiner="katya.zadorozhna.00@gmail.com"

ENV PYTHONBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt

RUN apk update \
    && apk add --no-cache libpq gcc musl-dev postgresql-dev jpeg-dev zlib-dev

RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /vol/web/media

RUN adduser \
    --disabled-password \
    --no-create-home \
    django-user

RUN chown -R django-user:django-user /vol/
RUN chmod -R 755 /vol/web/

USER django-user
