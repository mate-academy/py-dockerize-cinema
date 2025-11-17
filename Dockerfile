# Base image
FROM python:3.11-alpine

# Install system dependencies
RUN apk add --no-cache gcc musl-dev libffi-dev jpeg-dev zlib-dev postgresql-dev bash procps

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project code
COPY . .

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Default command (can be overridden in docker-compose)
CMD ["sh"]
