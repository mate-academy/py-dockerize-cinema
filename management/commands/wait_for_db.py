from django.core.management.base import BaseCommand
from django.db import OperationalError
from django.db import connections
import time


class Command(BaseCommand):
    help = "Wait for database"

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")

        while True:
            try:
                connections["default"].ensure_connection()
                break
            except OperationalError:
                self.stdout.write("Database unavailable, waiting...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available!"))
