# syntax=docker/dockerfile:1
FROM python:3.11-slim

# Prevents Python from writing .pyc files and buffers
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install system deps for psycopg (v3) and Pillow
RUN apt-get update \
 && apt-get install -y --no-install-recommends gcc libpq-dev build-essential libjpeg-dev zlib1g-dev \
 && rm -rf /var/lib/apt/lists/*

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Copy entrypoint script and make executable
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Expose app port
EXPOSE 8000

# Run entrypoint (handles wait_for_db, migrate, collectstatic, etc.)
ENTRYPOINT ["/entrypoint.sh"]

# Run Gunicorn with 3 workers for Django WSGI app
CMD ["gunicorn", "cinema_service.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]

