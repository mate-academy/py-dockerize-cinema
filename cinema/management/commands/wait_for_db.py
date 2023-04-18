import time

from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    """Django management command to wait for database to be available"""

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")

        db_conn = None
        while not db_conn:
            try:
                # Attempt to get a database connection
                db_conn = connections["default"]
            except OperationalError:
                # If the connection fails, wait for a second
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available!"))
