import time

from django.core.management import BaseCommand
from django.db import (
    OperationalError,
    connections
)


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Waiting for Postgres database...")
        db_conn = connections["default"]
        retries = 5

        for retry in range(retries):
            try:
                db_conn.cursor()
                self.stdout.write("Database available!")
                return
            except OperationalError:
                self.stdout.write(f"Retry {retry} to connect to Postgres")
                time.sleep(2)
        raise OperationalError(f"Database not ready after {retries} retries")
