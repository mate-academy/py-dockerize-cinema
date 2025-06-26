import time
from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    help = "Waits for the database to become available"

    def handle(self, *args, **kwargs):
        self.stdout.write("Waiting for database...")

        while True:
            try:
                with connections["default"].cursor():
                    break
            except OperationalError:
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available!"))
