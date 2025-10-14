#!/bin/sh

set -e

echo "Waiting for database to be ready..."
python manage.py wait_for_db

echo "Running migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

mkdir -p /app/media

echo "Starting server..."
exec "$@"
