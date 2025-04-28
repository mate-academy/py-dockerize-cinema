FROM python:3.12-alpine3.18
LABEL maintainer="eugene2piskun@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR /app


COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN adduser \
    --disabled-password \
    --no-create-home \
    django-user

RUN mkdir -p /vol/web/media

RUN chown -R django-user:django-user /vol/
RUN chmod -R 755 /vol/web/

COPY . .