import time
from django.core.management.base import BaseCommand

from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    """The command to wait for db connections"""

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        db_connection = None
        while not db_connection:
            try:
                db_connection = connections["default"]
                db_connection.cursor()
            except OperationalError:
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)
            else:
                self.stdout.write("Database available.")
