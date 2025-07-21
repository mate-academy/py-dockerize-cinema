FROM python:3.11.6-alpine3.18

LABEL maintainer="alopar632@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /vol/web/media

RUN adduser \
        --disabled-password \
        --no-create-home \
        django-user

RUN chown -R django-user:django-user /vol/
RUN chmod -R 755 /vol/web/
