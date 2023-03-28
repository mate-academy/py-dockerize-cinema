import time

from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        self.stdout.write("Waiting for database to be available...")
        db_connection = None
        while not db_connection:
            try:
                db_connection = connections["default"]
                self.stdout.write(self.style.SUCCESS("Database is available"))
            except OperationalError:
                self.stdout.write(
                    "Database is unavailable, waiting for 5 seconds..."
                )
                time.sleep(5)
