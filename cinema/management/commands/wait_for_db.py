import time

from django.core.management import BaseCommand
from django.db import connections, OperationalError


class Command(BaseCommand):
    help = "Wait for db to become available"

    def handle(self, *args, **options):
        self.stdout.write("Waiting for db to become available...")

        db_conn = connections["default"]
        while True:
            try:
                connection = db_conn.cursor()
                break
            except OperationalError:
                self.stdout.write(
                    self.style.WARNING("Database unavailable, waiting 1 second...")
                )
                time.sleep(1)

        self.stdout.write(
            self.style.SUCCESS("Successfully connected to cinema database")
        )
