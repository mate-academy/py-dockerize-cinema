FROM python:3.11.6-alpine3.18
LABEL authors="king.krollie@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r --no-cache-dir requirements.txt

COPY . .
