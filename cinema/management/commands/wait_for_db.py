import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        self.stdout.write("Waiting for database...")
        db_conn = None
        attempt = 0

        while not db_conn:
            try:
                db_conn = connections["default"]
                db_conn.cursor()
            except OperationalError:
                attempt += 1
                self.stdout.write(
                    f"Database unavailable, "
                    f"waiting 1 second... (attempt {attempt})")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available!"))
