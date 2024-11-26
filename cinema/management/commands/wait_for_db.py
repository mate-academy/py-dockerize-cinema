import time
from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    """Django command to wait for the database to be available"""

    def handle(self, *args, **kwargs):
        self.stdout.write("Waiting for database...")
        max_retries = 5
        retry_delay = 2
        for _ in range(max_retries):
            try:
                db_conn = connections["default"]
                db_conn.cursor()
                self.stdout.write(self.style.SUCCESS("Database is available!"))
                break
            except OperationalError:
                self.stdout.write(
                    f"Database unavailable, retrying in {retry_delay}s..."
                )
                time.sleep(retry_delay)
        else:
            self.stderr.write(
                self.style.ERROR(
                    "Database is unavailable after max retries."
                )
            )
            raise OperationalError("Database unavailable after max retries.")
