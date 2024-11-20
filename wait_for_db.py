import os
import time
import django
from django.db import connections
from django.db.utils import OperationalError

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cinema_service.settings")
django.setup()

def wait_for_db():
    print("Waiting for database...")
    db_up = False
    while not db_up:
        try:
            conn = connections["default"]
            conn.cursor()
            db_up = True
        except OperationalError:
            print("Database unavailable, waiting 1 second...")
            time.sleep(1)
    print("Database available!")

if __name__ == "__main__":
    wait_for_db()