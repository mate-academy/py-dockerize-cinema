FROM python:3.11-slim
LABEL maintainer="admin@admin.com"

RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /vol/web/media /vol/web/static

RUN adduser --disabled-password --no-create-home django-user
RUN chown -R django-user:django-user /vol/
RUN chmod -R 755 /vol/web/
USER django-user
