#!/bin/bash
set -e

chown -R django-user:django-user /vol/web

exec gosu django-user python manage.py wait_for_db && \
     python manage.py migrate && \
     python manage.py collectstatic --no-input && \
     python manage.py runserver 0.0.0.0:8000
