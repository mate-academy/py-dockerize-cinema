import time

from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError
from psycopg2 import OperationalError as Psycopg2OpError


class Command(BaseCommand):
    """Django command to wait for the database to be available."""

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        db_up = False
        while not db_up:
            try:
                connections["default"].cursor()
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available!"))
