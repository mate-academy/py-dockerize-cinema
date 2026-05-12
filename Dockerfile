FROM python:3.13-slim
LABEL maintainer="ilchuk.cergey@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /upload/media
RUN mkdir -p /upload/static

RUN adduser \
    --disabled-password \
    --no-create-home \
    django_user

RUN chown -R django_user /upload/media
RUN chmod -R 755 /upload/media
RUN chown -R django_user /upload/static
RUN chmod -R 755 /upload/static

USER django_user
