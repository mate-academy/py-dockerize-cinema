import time
from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Waiting for the database..."))
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections["default"]
            except OperationalError:
                self.stdout.write(self.style.WARNING(
                    "Database unavailable, retrying in 1 second..."
                ))
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database is available!"))
