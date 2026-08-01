from django.core.management.base import BaseCommand
from django.db.utils import OperationalError
from psycopg2 import OperationalError as Psycopg2OperationalError
from django.db import connections
import time


class Command(BaseCommand):
    """Wait for database to become available."""

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")

        db_conn = None

        while db_conn is None:
            try:
                db_conn = connections["default"]
                db_conn.cursor()
            except (OperationalError, Psycopg2OperationalError):
                self.stdout.write(
                    "Database unavailable, waiting 1 second..."
                )
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available!"))
