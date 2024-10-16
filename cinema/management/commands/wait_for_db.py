import time

from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        db_conn = None
        max_attempts = 5
        attempts = 0

        while not db_conn and attempts < max_attempts:
            try:
                connections["default"].ensure_connection()
                db_conn = connections["default"]
            except OperationalError:
                attempts += 1
                self.stdout.write(f"Database unavailable, waiting 1 second... (Attempt {attempts}/{max_attempts})")
                time.sleep(1)

        if db_conn:
            self.stdout.write(self.style.SUCCESS("Database connection established!"))
        else:
            self.stdout.write(self.style.ERROR("Database not available after max attempts."))
