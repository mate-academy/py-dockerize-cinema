FROM python:3.12-slim
LABEL maintainer="olga.gynguliak@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /files/media files/staticfiles
