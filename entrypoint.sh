#!/bin/sh

python manage.py wait_for_db


# Perform Django database migrations
python manage.py makemigrations
python manage.py migrate


# Start Django development server
python manage.py runserver 0.0.0.0:8000
