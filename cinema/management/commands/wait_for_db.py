import time

from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    help_text = "Waits for the database to be available."

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        while True:
            try:
                connections["default"].ensure_connection()
                break
            except OperationalError:
                self.stdout.write("Database unavailable, retrying in 1s...")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("Database available!"))
