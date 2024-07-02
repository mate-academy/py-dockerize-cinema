FROM python:3.12.0-alpine
LABEL authors="agrytsai"

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /files/media/uploads/movies

RUN adduser \
    --disabled-password \
    --no-create-home \
    maine_us

RUN chown -R maine_us:maine_us /files
RUN chmod -R 777 /files


USER maine_us
