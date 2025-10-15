FROM python:3.11-slim

# Prevent Python from writing .pyc files and output buffering
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies only for build
RUN apt-get update \
 && apt-get install -y --no-install-recommends gcc libpq-dev build-essential libjpeg-dev zlib1g-dev \
 && rm -rf /var/lib/apt/lists/*

# Copy and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt \
 && apt-get remove --purge -y gcc build-essential \
 && apt-get autoremove -y \
 && rm -rf /var/lib/apt/lists/*

# Copy entrypoint first so rebuilds are faster if only code changes
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Copy project files
COPY . .

# Optional: Create non-root user for better security
RUN adduser --disabled-password --gecos '' appuser \
 && chown -R appuser /app
USER appuser

# Expose app port
EXPOSE 8000

# Run entrypoint (handles wait_for_db, migrate, collectstatic, etc.)
ENTRYPOINT ["/entrypoint.sh"]

# Run Gunicorn with 3 workers for Django WSGI app
CMD ["gunicorn", "cinema_service.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
