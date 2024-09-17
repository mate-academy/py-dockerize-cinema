import time
from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Waiting for database connection...")
        db_conn = None

        while not db_conn:
            try:
                db_conn = connections["default"]
            except OperationalError:
                self.stdout.write(
                    "Database connection unavailable, please wait..."
                )
                time.sleep(2)

        self.stdout.write(self.style.SUCCESS(
            "Database connection established!"
        ))
