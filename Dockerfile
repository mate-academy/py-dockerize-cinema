FROM python:3.14.7-alpine3.24
LABEL maintainer="mikhailetc.artem@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN mkdir -p /vol/web/media /vol/web/static


RUN adduser -D -H django-user

RUN chown -R django-user:django-user /vol/
RUN chmod -R 755 /vol/web/


USER django-user
