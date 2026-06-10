FROM python:3.10-slim
LABEL maintainer="oleks@example.com"

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

RUN adduser \
    --disabled-password \
    --no-create-home \
    django-user

RUN chown -R django-user:django-user /vol/
RUN chmod -R 755 /vol/

USER django-user
