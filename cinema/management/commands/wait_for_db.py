import time

from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Waiting...")
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections["default"].cursor()
            except OperationalError:
                self.stdout.write(
                    "Database unavailable, waiting 0.5 second..."
                )
                time.sleep(0.5)
        self.stdout.write(self.style.SUCCESS(
            "Successfully connected to database"
        )
        )
