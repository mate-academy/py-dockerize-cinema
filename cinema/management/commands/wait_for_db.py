import time
from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Waiting for the database...")
        db_conn = None
        attempts = 0
        max_attempts = 30  # You can adjust this based on your needs

        while not db_conn and attempts < max_attempts:
            try:
                db_conn = connections["default"]
            except OperationalError:
                attempts += 1
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)

        if db_conn:
            self.stdout.write(self.style.SUCCESS("Database is available!"))
        else:
            self.stdout.write(
                self.style.ERROR(
                    "Unable to establish a connection to the database"
                )
            )
