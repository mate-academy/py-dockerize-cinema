FROM python:3.11.9-slim
LABEL authors="specializeddev"

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /files/media

RUN adduser --disabled-password --no-create-home django-user

RUN chown -R django-user:django-user /files/media
RUN chmod -R 755 /files/media/

USER django-user