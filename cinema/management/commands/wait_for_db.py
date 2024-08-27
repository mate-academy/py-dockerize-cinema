import time
from django.core.management.base import BaseCommand
from django.db import OperationalError, connections


class Command(BaseCommand):

    def handle(self, *args, **options) -> None:
        database_connection = None

        self.stdout.write("Waiting for database...")

        while not database_connection:
            try:
                database_connection = connections["default"]
                database_connection.cursor()
            except OperationalError:
                self.stdout.write(
                    "Database is unavailable. Waiting 3 seconds..."
                )
                time.sleep(3)

        self.stdout.write("Database is available!")
