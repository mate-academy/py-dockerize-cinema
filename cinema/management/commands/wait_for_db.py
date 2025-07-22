import time

from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        self.stdout.write("Waiting for database...")
        db_connection = None
        while not db_connection:
            try:
                db_connection = connections["default"].cursor()
            except OperationalError:
                self.stdout.write(
                    "Database not available, waiting 1 second..."
                )
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("Database available!"))
