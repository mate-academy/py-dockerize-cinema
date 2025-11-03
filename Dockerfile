# Use official Python runtime as a base image
FROM python:3.11-alpine

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apk update && \
    apk add --no-cache \
        postgresql-client \
        jpeg-dev \
        zlib-dev && \
    apk add --no-cache --virtual .build-deps \
        gcc \
        musl-dev \
        postgresql-dev && \
    pip install --upgrade pip

# Copy requirements file
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt && \
    apk del .build-deps

# Copy project files
COPY . /app/

# Create directories for media and static files
RUN mkdir -p /app/media /app/staticfiles

# Create a non-root user
RUN adduser -D appuser && \
    chown -R appuser:appuser /app

USER appuser
