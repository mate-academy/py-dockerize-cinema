import time

from django.core.management import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    help = "Wait for the database to be available"  # noqa: VNE003

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        while True:
            try:
                connections["default"].ensure_connection()
                break
            except OperationalError:
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available!"))
