import time
from django.db import connections
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to pause execution until database is available"""

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database... 10 sec till timeout")
        timeout_wait = 0
        db_connection = None
        while not db_connection and timeout_wait < 10:
            timeout_wait += 1
            try:
                db_connection = connections["default"]
            except Exception:
                self.stdout.write(
                    f"Database unavailable, waiting {timeout_wait} second...")
                time.sleep(1)
            if timeout_wait == 10:
                raise Exception("Database unavailable")

        self.stdout.write(self.style.SUCCESS("Database available!"))
