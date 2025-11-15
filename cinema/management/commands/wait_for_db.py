import time

from django.core.management import BaseCommand
from django.db import connections
from django.db import OperationalError


class Command(BaseCommand):
    def handle(self, *args, **options):
        while True:
            try:
                _ = connections["default"]
                self.stdout.write(
                    self.style.SUCCESS("Successfully connected to PostgreSQL")
                )
                return 0
            except OperationalError:
                time.sleep(1)
                self.stdout.write("Waiting for connection...")
