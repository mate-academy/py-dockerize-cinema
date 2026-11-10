import time
from django.core.management.base import BaseCommand
from django.db import OperationalError, connections


class Command(BaseCommand):

    def handle(self, *args):
        """
        Waits for the database to be available before continuing.
        """
        self.stdout.write("Waiting for database...")

        db_conn = None
        while not db_conn:
            try:
                db_conn = connections["default"]
                db_conn.cursor()
            except OperationalError:
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database is available!"))
