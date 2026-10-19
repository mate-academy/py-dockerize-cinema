import time

from django.core.management.base import BaseCommand
from django.db import connection
from django.db.utils import OperationalError
from psycopg2 import OperationalError as Psycopg2OpError


class Command(BaseCommand):
    """Django command to wait for the database to be available."""

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        db_ready = False
        while not db_ready:
            try:
                connection.ensure_connection()
                db_ready = True
            except (OperationalError, Psycopg2OpError):
                self.stdout.write(
                    "Database unavailable, waiting 1 second..."
                )
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available!"))
