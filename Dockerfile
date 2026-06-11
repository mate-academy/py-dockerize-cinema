FROM python:3.10.8-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt


RUN adduser --disabled-password --no-create-home django-user

RUN mkdir -p /files/staticfiles /files/mediafiles

RUN chown -R django-user:django-user /files/
RUN chmod -R 755 /files/
USER django-user

COPY . .
