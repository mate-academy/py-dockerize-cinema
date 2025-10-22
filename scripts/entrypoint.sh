#!/bin/sh

set -e

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for database..."
    python manage.py wait_for_db
    echo "Database available!"
fi

echo "Applying database migrations..."
python manage.py migrate

python manage.py collectstatic --noinput

exec "$@"