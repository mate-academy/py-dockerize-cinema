#!/bin/sh

set -e

host="$1"
shift
cmd="$@"

POSTGRES_USER="${POSTGRES_USER:-cinema}"
POSTGRES_DB="${POSTGRES_DB:-cinema}"
POSTGRES_PASSWORD="${POSTGRES_PASSWORD:-cinema}"

>&2 echo "Waiting for Postgres at $host (db: $POSTGRES_DB, user: $POSTGRES_USER)..."

until PGPASSWORD=$POSTGRES_PASSWORD psql -h "$host" -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c '\q' >/dev/null 2>&1; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - executing command"
exec $cmd
