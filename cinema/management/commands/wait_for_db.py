import time

from django.core.management import BaseCommand
from django.db import connections, OperationalError


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("waiting for db...")
        while True:
            db_conn = connections["default"]
            db_conn.cursor()
            if db_conn is not None:
                break
            self.stdout.write(
                "Database unavailable, waiting for 1 second...")
            time.sleep(1)
        self.stdout.write(self.style.SUCCESS("Database available!"))
