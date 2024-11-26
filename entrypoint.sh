#!/bin/sh

echo "Waiting for database to be ready..."
python manage.py wait_for_db

echo "Starting Django server..."
exec "$@"
