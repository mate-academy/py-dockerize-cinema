import time

from django.core.management.base import BaseCommand
from django.db import connections, OperationalError


class Command(BaseCommand):
    """Checks if connection to the default
     database was established, retries until successful"""

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database to become available...")

        db_conn = None
        while db_conn is None:
            try:
                db_conn = connections["default"]
                db_conn.cursor()
            except OperationalError:
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available."))
