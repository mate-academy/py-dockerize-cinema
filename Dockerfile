FROM python:3.12-alpine
LABEL authors="user"

ENV PYTHONUNBUFFERED=1

WORKDIR app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p files/media
