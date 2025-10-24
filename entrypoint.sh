#!/bin/sh
cd /app

echo
python manage.py wait_for_db

echo
python manage.py migrate --noinput

echo
exec "$@"