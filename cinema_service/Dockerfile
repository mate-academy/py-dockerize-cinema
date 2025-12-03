FROM python:3.11-slim
LABEL maintainer="cinema-service"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    postgresql-client \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Create directories for static and media files
RUN mkdir -p /vol/web/media /vol/web/static

# Create non-root user
RUN adduser \
    --disabled-password \
    --no-create-home \
    django-user

# Set ownership of volumes
RUN chown -R django-user:django-user /vol/
RUN chmod -R 755 /vol/web

# Switch to non-root user
USER django-user