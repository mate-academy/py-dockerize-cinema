import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Command to pause execution until database is available"""

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        db_conn = None
        attempt = 0
        max_attempts = 30
        verbosity = options.get("verbosity", 1)

        while db_conn is None and attempt < max_attempts:
            try:
                db_conn = connections["default"].cursor()
            except OperationalError:
                if verbosity > 0:
                    self.stdout.write(
                        "Database unavailable, waiting 1 second..."
                    )
                time.sleep(1)
                attempt += 1

        if db_conn:
            self.stdout.write(self.style.SUCCESS("Database available!"))
        else:
            self.stdout.write(
                self.style.ERROR(
                    "Failed to connect to database after several attempts"
                )
            )
