FROM python:3.11-slim
LABEL maintainer="bileichuk.ivan@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /app/media && \
    adduser --disabled-password --no-create-home my_user && \
    chown -R my_user /app && \
    chmod -R 755 /app/media

USER my_user
