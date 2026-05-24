import time
from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    """Wait for db connection"""

    def handle(self, *args, **options):
        self.stdout.write("Checking database connection...")

        db_conn = None
        attempts = 0
        while not db_conn and attempts < 15:
            try:
                db_conn = connections["default"]
                db_conn.cursor()
            except OperationalError:
                attempts += 1
                self.stdout.write(
                    f"DB is not ready(attempt {attempts}/15)... "
                    f"Wait for 2 seconds."
                )
                time.sleep(2)
            else:
                self.stdout.write(
                    self.style.SUCCESS("DB is ready, continue...")
                )
