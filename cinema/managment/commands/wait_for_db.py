import time

from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        self.stdout.write("Waiting for database...")
        db_connect = None
        attempt = 0

        while not db_connect:
            try:
                db_connect = connections["default"]
                db_connect.cursor()
            except OperationalError:
                attempt += 1
                self.stdout.write(
                    f"Database unavailable, waiting 1 second... "
                    f"(Attempt {attempt})"
                )
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database is ready!"))
