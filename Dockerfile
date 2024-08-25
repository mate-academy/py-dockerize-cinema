FROM python:3.12-slim

LABEL maintainer="boris.tikhonov.21@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .


RUN mkdir -p web/media


RUN adduser \
         --disabled-password \
         --no-create-home \
         django-user

RUN chown -R django-user:django-user web/media
RUN chmod -R 755 web/media

