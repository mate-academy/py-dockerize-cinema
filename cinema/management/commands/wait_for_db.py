import time

from django.core.management.base import BaseCommand
from django.db import OperationalError, connections


class Command(BaseCommand):
    """Wait until the configured database accepts connections."""

    help = "Wait for the database to become available"

    def handle(self, *args, **options):  # noqa
        self.stdout.write("Waiting for database...")
        while True:
            try:
                connections["default"].ensure_connection()
            except OperationalError:
                self.stdout.write(
                    "Database unavailable; retrying in 1 second."
                )
                time.sleep(1)
            else:
                self.stdout.write(self.style.SUCCESS("Database is available."))
                break
