FROM python:3.11-slim

RUN apt-get update \
  && apt-get install -y build-essential libpq-dev \
  && apt-get clean

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x ./manage.py
