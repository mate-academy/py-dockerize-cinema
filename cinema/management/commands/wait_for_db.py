import time

from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    """Wait until the default database accepts connections."""

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        database_ready = False
        while not database_ready:
            try:
                connections["default"].ensure_connection()
                database_ready = True
            except OperationalError:
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database is available."))
