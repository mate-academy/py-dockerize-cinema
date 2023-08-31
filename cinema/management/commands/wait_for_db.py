"""
Django command to wait for the database to be available.
"""
import time

from psycopg2 import OperationalError as Psycopg2OpError

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to pause execution until the database is available"""

    def handle(self, *args, **kwargs):
        self.stdout.write("Waiting for database...")
        db_conn = None
        max_attempts = 5
        attempts = 0

        while not db_conn:
            try:
                self.check(databases=["default"])
                db_conn = True
            except (Psycopg2OpError, OperationalError) as e:
                attempts += 1
                if attempts >= max_attempts:
                    self.stdout.write(
                        self.style.ERROR(
                            "Max attempts reached. "
                            "Could not connect to database."
                        )
                    )
                    raise e
                self.stdout.write(
                    self.style.WARNING(
                        "Database unavailable, waiting 1 second..."
                    )
                )
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available!"))
