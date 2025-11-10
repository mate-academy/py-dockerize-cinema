import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    """Command tp pause execution until database is available"""

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        db_conn = None
        db_up = False
        while not db_up:
            try:
                db_conn = connections["default"]
                db_conn.cursor()
                db_up = True
            except OperationalError:
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS(
            "Database available! Waiting 2 more seconds..."
        ))
        time.sleep(2)

        self.stdout.write(self.style.SUCCESS("Continuing startup."))
