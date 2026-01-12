#!/bin/sh
python manage.py wait_for_db
python manage.py collectstatic --noinput
python manage.py migrate
exec gunicorn cinema_service.wsgi:application --bind 0.0.0.0:8000
