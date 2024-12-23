#!/bin/sh

# Wait for database to be available.
python manage.py wait_for_db

# Run migrations.
python manage.py makemigrations
python manage.py migrate

# Start the server.
python manage.py runserver 0.0.0.0:8000