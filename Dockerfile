FROM python:3.11.6-alpine3.18
LABEL maintainer="liza.shulika.2009+1@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .