FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN adduser \
    --disabled-password \
    --no-create-home \
    django-user


RUN mkdir -p /vol/web/static \
    && mkdir -p /vol/web/media \
    && chown -R django-user:django-user /vol/web/static \
    && chown -R django-user:django-user /vol/web/media \
    && chmod -R 755 /vol/web/static \
    && chmod -R 755 /vol/web/media

RUN mkdir -p /vol/web

USER django-user
