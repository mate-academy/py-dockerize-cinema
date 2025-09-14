FROM python:3.13-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /files/media

RUN adduser --disabled-password --no-create-home my_user

RUN chown -R my_user /files/media
RUN chown -R 755 /files/media
USER my_user