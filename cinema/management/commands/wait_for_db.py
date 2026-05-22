from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError
import time


class Command(BaseCommand):
    """Django command to pause execution until database is available"""

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...", ending="")

        attempts = 0
        max_attempts = 30
        db_ready = False

        while attempts < max_attempts:
            try:
                connections["default"].cursor()
                db_ready = True
                break
            except OperationalError:
                self.stdout.write(
                    "Database unavailable, waiting for a 1 second",
                    ending=""
                )
                attempts += 1
                time.sleep(1)

        if not db_ready:
            raise Exception("Database not available after max attempts")

        self.stdout.write(self.style.SUCCESS("Database available!"))
