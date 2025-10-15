set -e

echo "Waiting for database to be ready..."
python manage.py wait_for_db

echo "Running migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
mkdir -p /app/staticfiles
python manage.py collectstatic --noinput

echo "Ensuring media directory exists..."
mkdir -p /app/media

echo "Starting server..."
exec "$@"
