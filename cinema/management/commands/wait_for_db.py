from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError
import time


class Command(BaseCommand):
    """Django command to pause execution until database is available"""

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...", ending="")

        db_conn = None

        while not db_conn:
            try:
                db_conn = connections["default"]
                self.stdout.write(
                    "Database unavailable, waiting for a 1 second",
                    ending=""
                )
                db_conn.cursor()
            except OperationalError:
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available!"))
