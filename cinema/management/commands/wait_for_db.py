import time
from os import getenv

from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        db_conn = self.establish_db_connection()
        if db_conn:
            self.stdout.write(self.style.SUCCESS(
                "Database connection established!"
            ))
        else:
            self.stdout.write(self.style.ERROR(
                "Database not available after max attempts."
            ))

    def establish_db_connection(self):
        max_attempts = int(getenv("MAX_ATTEMPTS"))
        for attempt in range(1, max_attempts + 1):
            if self.try_connection():
                return connections["default"]
            self.log_connection_attempt(attempt, max_attempts)
            time.sleep(1)
        return None

    def try_connection(self):
        try:
            connections["default"].ensure_connection()
            return True
        except OperationalError:
            return False

    def log_connection_attempt(self, attempt, max_attempts):
        self.stdout.write(
            f"Database unavailable, waiting 1 second... "
            f"(Attempt {attempt}/{max_attempts})"
        )
