FROM python:3.9-slim
LABEL maintainer="simplemanua@gmail.com"

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt requirements.txt

RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && pip install -r requirements.txt \
    && apt-get remove -y gcc \
    && apt-get autoremove -y

WORKDIR /app
COPY . .

RUN mkdir -p /files/media

RUN adduser --disabled-password --no-create-home django-user

# Set permissions for media folder to django-user
RUN chown -R django-user /files/media
RUN chmod -R 755 /files/media

USER django-user
