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
                connection = connections["default"]
                connection.close()
                db_connection = True
            except OperationalError:
                self.stdout.write("Database connection failed.")
                time.sleep(1)
        self.stdout.write("Database connection successful.")
