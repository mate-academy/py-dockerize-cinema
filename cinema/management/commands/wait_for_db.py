import time

from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    """Wait command for check if database ready to connect."""

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        conn = False
        delay = 5

        while not conn:
            try:
                connections["default"].ensure_connection()
                conn = True
            except OperationalError:
                self.stdout.write(
                    f"Database is not ready. Next try after {delay} seconds"
                )
                time.sleep(delay)

        self.stdout.write("Database is ready. Starting app...")
