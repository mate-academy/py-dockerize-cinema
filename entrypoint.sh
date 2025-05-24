#!/bin/sh

set -e

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for PostgreSQL to become available..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 1
    done

    echo "PostgreSQL is ready"
fi

python manage.py wait_for_db
python manage.py migrate --no-input
python manage.py collectstatic --no-input --clear

exec "$@"
