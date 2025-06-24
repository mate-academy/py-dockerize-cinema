FROM python:3.12-slim
LABEL maintainer="tarashevchik27@gmail.com"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

RUN adduser --disabled-password --no-create-home django-user

COPY . .

RUN mkdir -p /app/media/uploads/movies /app/static && \
    chown -R django-user:django-user /app/media /app/static && \
    chmod -R 775 /app/media /app/static

USER django-user
