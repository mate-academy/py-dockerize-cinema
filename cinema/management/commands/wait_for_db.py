import time

from django.core.management import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        db_connection = None

        while not db_connection:
            try:
                db_connection = connections["default"]
                db_connection.cursor()
            except OperationalError:
                self.stdout.write(
                    "Database unavailable, trying again in 1 second..."
                )
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database ready"))
