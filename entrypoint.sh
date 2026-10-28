#!/bin/sh
set -e

mkdir -p /vol/web/static /vol/web/media || true
chown -R appuser:appuser /vol/web/static /vol/web/media || true

python manage.py wait_for_db
python manage.py migrate --noinput
python manage.py collectstatic --noinput

exec su -s /bin/sh appuser -c"gunicorn cinema_service.wsgi:application
--bind 0.0.0.0:8000 --workers 3"
