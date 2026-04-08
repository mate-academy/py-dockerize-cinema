FROM python:3.11-slim
LABEL maintainer="taras.mosiichuk.01@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN mkdir -p /files/media /files/static

RUN adduser \
    --disabled-password \
    --no-create-home \
    my_user

RUN chown -R my_user /files/media /files/static
RUN chmod -R 755 /files/media /files/static

USER my_user
