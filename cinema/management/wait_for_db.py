import time

from django.core.management import BaseCommand
from django.db import connections, OperationalError


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        connection = None
        while not connection:
            try:
                connection = connections["default"]
                connection.cursor().execute("SELECT 1")
            except OperationalError:
                self.stdout.write("Database unavailable, waiting 1 second...")
                connection = None
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available!"))
