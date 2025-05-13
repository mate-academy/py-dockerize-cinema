FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt ./

#RUN apt-get update && apt-get install -y \
#    libpq-dev \
#    gcc
RUN python -m pip install --no-cache-dir -r requirements.txt

COPY . .
RUN mkdir -p /files/media
EXPOSE 8000

RUN adduser --disabled-password --no-create-home django-user && \
    mkdir -p /files/media /files/static && \
    chown -R  django-user /files && \
    chmod -R 755 /files
USER django-user


