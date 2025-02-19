import os
import time
import django
from django.db import connections
from django.db.utils import OperationalError


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cinema_service.settings")
django.setup()

def wait_for_db():
    print("Очікування бази даних...")
    db_conn = None

    while not db_conn:
        try:
            db_conn = connections['default']
            db_conn.cursor()
            print("База даних доступна!")
            break
        except OperationalError:
            print("База даних ще не готова, чекаємо 2 секунди...")
            time.sleep(2)

if __name__ == "__main__":
    wait_for_db()
