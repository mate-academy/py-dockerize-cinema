import time
from sqlite3 import OperationalError

from django.core.management import BaseCommand

from django.db import connections


class Command(BaseCommand):
    help = "Wait for database to be ready." # noqa

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database to be ready...")
        database_connection = None
        max_attempts = 30
        attempt = 0

        while database_connection is None and attempt < max_attempts:
            try:
                database_connection = connections["default"]
                database_connection.cursor()
            except OperationalError:
                attempt += 1
                self.stdout.write(
                    f"Database unavailable,"
                    f" waiting 1 second... (Attempt {attempt}/{max_attempts})"
                )
                time.sleep(1)

        if database_connection is None:
            self.stdout.write(self.style.ERROR("Database not ready."))
            raise Exception("Database is not available.")

        self.stdout.write(self.style.SUCCESS("Database ready."))
