import time
from django.db import connection
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command that waits for database  to be abailable"""

    def handle(self, *args, **options):
        """Handle the command"""
        self.stdout.write("Waiting for database.....")
        db_connection = None
        while not db_connection:
            try:
                connection.ensure_connection()
                db_connection = True
            except OperationalError:
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available!"))
