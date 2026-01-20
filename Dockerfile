# Use slim Python image for minimal size
FROM python:3.11-alpine
LABEL maintainer="devpsychologist"

ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install -r requirements.txt

# Copy application code
COPY . .

RUN mkdir -p /files/media

RUN adduser \
        --disabled-password \
        --no-create-home \
        django-user

RUN chown -R django-user:django-user /files /app
RUN chmod -R 755 /files

USER django-user
