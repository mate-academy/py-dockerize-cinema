import time

from django.core.management.base import BaseCommand
from django.db import connections, OperationalError


class Command(BaseCommand):
    """Command to pause execution until db is available"""

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database..")
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections["default"]
                db_conn = True
            except OperationalError:
                self.stdout.write("Database is unavailable, please wait..")
                time.sleep(1)

        self.stdout.write("Database is available.")
