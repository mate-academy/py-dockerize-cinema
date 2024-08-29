FROM python:3.11-slim
LABEL maintainer="playfog3@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /media

RUN adduser \
    --disabled-password \
    --no-create-home \
    user

RUN chown -R user /media
RUN chmod -R 755 /media

USER user
