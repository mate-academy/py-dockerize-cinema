import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    helps = "Waits for the database to be available"

    def handle(self, *args, **kwargs):
        self.stdout.write("Waiting for database to be available")
        db_connection = None
        while not db_connection:
            try:
                db_connection = connections["default"]
                self.stdout.write(self.style.SUCCESS("Database available!"))
            except OperationalError:
                self.stdout.write("Database unavailable, waiting 1 second")
                time.sleep(1)
