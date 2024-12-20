FROM python:3.12.0-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/app" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    django-user

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy application files and ensure correct ownership
COPY . .
RUN mkdir -p /app/media && \
    chown -R django-user /app/media && \
    chmod -R 755 /app/media && \
    chown -R django-user /app

# Switch to non-root user
USER django-user

