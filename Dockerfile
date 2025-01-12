FROM python:3.9.7-alpine3.14

LABEL authors="frezworx"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN  pip install --upgrade pip && \
     pip install --no-cache-dir -r requirements.txt

RUN mkdir -p /files/media
COPY . .


RUN adduser --disabled-password --no-create-home my-user

RUN chown -R my-user:my-user /app /files/media && \
RUN chmod -R 700 /files/media

USER my-user