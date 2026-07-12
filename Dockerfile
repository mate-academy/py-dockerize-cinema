# Use a slim official image to ensure the container is as thin as possible
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system dependencies needed for PostgreSQL (libpq) and image handling (Pillow)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . /app/

# Create directories for static and media files
RUN mkdir -p /app/staticfiles /app/media

# Create a non-privileged user to run the app safely
RUN useradd -U appuser && chown -R appuser:appuser /app
USER appuser
