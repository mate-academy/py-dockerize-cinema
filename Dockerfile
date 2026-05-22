FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN adduser \
    --disabled-password \
    --no-create-home \
    django-user

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

RUN chown -R django-user:django-user /vol/
RUN chown -R django-user:django-user /app

USER django-user