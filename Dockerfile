# syntax=docker/dockerfile:1

FROM python:3.11-alpine

# Prevent Python from writing .pyc files and buffering
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install runtime dependencies only (no build tools)
RUN apk add --no-cache \
    libpq \
    jpeg \
    zlib \
    bash \
    tzdata

WORKDIR /app

# Copy and install dependencies (ensure requirements use psycopg[binary] and Pillow wheels)
COPY requirements.txt .
RUN pip install --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Copy entrypoint and make executable
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Create non-root user and adjust permissions
RUN adduser -D appuser \
 && chown -R appuser:appuser /app
USER appuser

# Expose app port
EXPOSE 8000

# Entrypoint and command
ENTRYPOINT ["/entrypoint.sh"]
CMD ["gunicorn", "cinema_service.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
