import time
from django.core.management.base import BaseCommand, CommandError
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    """Waits for database to be available before continuing."""

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        success = False
        retries = 0
        max_retries = 10
        while not success and retries < max_retries:
            try:
                connections["default"].cursor()
            except OperationalError:
                retries += 1
                self.stdout.write(
                    "Database unavailable, waiting 1 second... "
                    f"(attempt {retries})"
                )
                time.sleep(1)
                continue
            success = True
            break
        if not success:
            raise CommandError("Could not connect to database after several attempts.")
        self.stdout.write(self.style.SUCCESS("Database available!"))
