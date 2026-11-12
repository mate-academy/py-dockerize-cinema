import time

from django.core.management import BaseCommand
from django.db import connections, OperationalError


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        while True:
            try:
                connections["default"].ensure_connection()
                self.stdout.write(self.style.SUCCESS("Database is available!"))
                break

            except OperationalError:
                time.sleep(1)
