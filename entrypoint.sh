#!/bin/sh

set -e

# Wait for the database to be available
python manage.py wait_for_db

# Apply database migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

exec "$@"
