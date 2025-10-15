import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Waits for the database to be available before continuing."

    def handle(self, *args, **options) -> None:
        self.stdout.write(self.style.WARNING("Waiting for database..."))
        attempt = 0

        while True:
            try:
                with connections["default"].cursor():
                    self.stdout.write(self.style.SUCCESS("Database is available!"))
                    break
            except OperationalError:
                attempt += 1
                self.stdout.write(f"Attempt {attempt}: Database unavailable, retrying in 1 second...")
                time.sleep(1)
