#!/bin/sh

# Чекає, поки база даних стане доступною
/usr/local/bin/python manage.py wait_for_db

# Виконує міграції
/usr/local/bin/python manage.py migrate

# Збирає статичні файли
/usr/local/bin/python manage.py collectstatic --noinput

# Запускає Django-сервер
/usr/local/bin/python manage.py runserver 0.0.0.0:8000
