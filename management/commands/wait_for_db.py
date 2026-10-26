from django.core.management.base import BaseCommand
from django.db import OperationalError
from django.db import connections
import time


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")

        start = time.time()

        while True:
            try:
                connections["default"].ensure_connection()
                break
            except OperationalError:
                if time.time() - start > 30:
                    raise

                self.stdout.write("Database unavailable, waiting...")
                time.sleep(1)
