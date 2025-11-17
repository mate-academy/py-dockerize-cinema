import time

from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        retry_interval = 1
        while True:
            try:
                connections["default"].ensure_connection()
                break
            except OperationalError:
                self.stdout.write(f"Database unavailable, "
                                  f"retrying in {retry_interval}s...")
                time.sleep(retry_interval)
        self.stdout.write(self.style.SUCCESS("Database is available!"))
