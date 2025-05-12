FROM python:3.11.6-alpine3.18
LABEL maintainer="hryn.yuri@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
