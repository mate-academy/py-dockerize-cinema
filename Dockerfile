FROM python:3.11-slim
LABEL maintrainer="ngayka@gmail.com"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /cinema_service

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN adduser \
        --disabled-password \
        --no-create-home \
        django-user

COPY . .