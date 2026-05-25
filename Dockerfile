FROM python:3.11.15-alpine3.22

LABEL maintainer="yukhnenko.o@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
RUN mkdir -p /files/media
RUN mkdir -p /app/staticfiles

RUN adduser \
    --disabled-password \
    --no-create-home \
    my_user

RUN chown -R my_user /files/media /app/staticfiles
RUN chmod -R 755 /files/media /app/staticfiles

USER my_user
