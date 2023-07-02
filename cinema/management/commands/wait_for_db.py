import time
from django.db import connection
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command that waits for the database to be available"""

    def handle(self, *args, **options):
        """Handle the command"""
        self.stdout.write("Waiting for the database...")
        retry_count = 0

        while True:
            try:
                connection.ensure_connection()
                break
            except OperationalError:
                if retry_count >= 5:
                    self.stdout.write("Unable to connect to the database.")
                    return
                self.stdout.write("Database unavailable,"
                                  " waiting 5 seconds...")
                time.sleep(5)
                retry_count += 1

        self.stdout.write(self.style.SUCCESS("Database available!"))
