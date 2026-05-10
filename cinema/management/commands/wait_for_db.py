import time

from django.core.management import BaseCommand
from django.db import connections, OperationalError


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("waiting for db...")
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections["default"]
                db_conn.cursor()
            except OperationalError:
                self.stdout.write(
                    "Database unavailable, waiting for 1 second...")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("Database available!"))
