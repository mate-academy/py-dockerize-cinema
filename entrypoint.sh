#!/usr/bin/env sh
set -eu

echo ">> Waiting for database..."
python manage.py wait_for_db

echo ">> Running: $*"
exec "$@"
