FROM python:3.12-alpine

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --default-timeout=120 -r requirements.txt

COPY . .

RUN mkdir -p /vol/web/media /vol/web/static

RUN adduser --disabled-password --no-create-home django-user

RUN chown -R django-user:django-user /vol/
RUN chmod -R 755 /vol/web/

USER django-user
