import time
from django.db import connection
from django.db.utils import OperationalError
from django.core.management import BaseCommand


class Command(BaseCommand):
    """Django command to pause execution until the database is available"""
    def handle(self, *args, **kwargs):
        self.stdout.write("Waiting for database...")

        while True:
            try:
                connection.ensure_connection()
            except OperationalError:
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)
            else:
                break

        self.stdout.write(self.style.SUCCESS("Database available!"))
