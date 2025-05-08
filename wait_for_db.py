import time
from django.db import connections
from django.db.utils import OperationalError


def wait_for_db():
    db_conn = None
    while db_conn is None:
        try:
            db_conn = connections["default"]
        except OperationalError:
            print("Database unavailable, waiting 1 second...")
            time.sleep(1)


if __name__ == "__main__":
    wait_for_db()
    print("Database is ready!")
