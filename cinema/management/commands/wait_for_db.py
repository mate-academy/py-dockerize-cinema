import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    command_help = "Pause execution until the database is available"

    def handle(self, *args, **kwargs):
        self.stdout.write("Waiting for the database to become available...")
        db_conn = None

        while not db_conn:
            try:
                db_conn = connections["default"]
                db_conn.cursor()
            except OperationalError:
                self.stdout.write(
                    "Database is not available yet. Waiting for 1 second..."
                )
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database is available!"))
