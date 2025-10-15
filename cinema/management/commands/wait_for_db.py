import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Waits for the database to be available before continuing."

    def handle(self, *args, **options) -> None:
        self.stdout.write(self.style.WARNING("Waiting for database..."))
        db_conn = None
        attempt = 0

        while not db_conn:
            try:
                db_conn = connections["default"]
                db_conn.cursor()
            except OperationalError:
                attempt += 1
                self.stdout.write(f"Attempt {attempt}: Database unavailable, retrying in 1 second...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database is available!"))
