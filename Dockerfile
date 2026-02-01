FROM python:3.11-alpine

LABEL maintainer="Jakub Paluch"

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN adduser \
    --disabled-password \
    --no-create-home \
    django-user \
    && chown -R django-user /app

RUN mkdir -p /vol/web/media /vol/web/static \
 && chown -R django-user:django-user /vol \
 && chmod -R 755 /vol/web


USER django-user

EXPOSE 8000
