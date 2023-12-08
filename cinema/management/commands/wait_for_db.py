import time

from django.core.management import BaseCommand
from django.db.utils import OperationalError
from django.db import connections


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Waiting for connect to DB...")
        connect = None
        while not connect:
            try:
                connect = connections["default"]
            except OperationalError:
                self.stdout.write(
                    "Database is unavailable, waiting fot db for 2 seconds..."
                )
                time.sleep(2)
        self.stdout.write(self.style.SUCCESS("Database is available!"))
