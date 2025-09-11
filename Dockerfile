FROM python:3.11-slim
LABEL maintainer="tamerlanpython@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
RUN mkdir -p /files/media/uploads

RUN chmod -R 755 /files/media
