#!/bin/sh
set -e

echo "Waiting for database to be ready..."
python manage.py wait_for_db

echo "Running migrations..."
python manage.py migrate --noinput

echo "Ensuring static and media directories exist..."
mkdir -p /app/staticfiles /app/media

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting server..."
exec "$@"
