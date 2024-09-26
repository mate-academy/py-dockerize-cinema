import time

from django.core.management import BaseCommand
from django.db.utils import OperationalError
from django.db import connections


class Command(BaseCommand):
    """
    Django command to pause execution until database is available
    """
    def handle(self, *args, **options):
        """Handle the command"""
        self.stdout.write("Waiting for database...")
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections["default"]
            except OperationalError:
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available!"))
