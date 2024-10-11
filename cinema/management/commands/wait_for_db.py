import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Wait for the database to be available...")
        db_connect = None
        max_attempts = 10
        attempts = 0
        while not db_connect and attempts < max_attempts:
            try:
                db_connect = connections["default"].ensure_connection()
            except OperationalError:
                attempts += 1
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)

        if not db_connect:
            self.stdout.write(self.style.ERROR(
                "Failed to connect to the database after multiple attempts."
            ))
        else:
            self.stdout.write(self.style.SUCCESS("Database available!"))
