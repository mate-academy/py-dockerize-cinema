#!/usr/bin/env bash
# exit on error
set -o errexit

python manage.py collectstatic --no-input
python manage.py wait_for_db
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
