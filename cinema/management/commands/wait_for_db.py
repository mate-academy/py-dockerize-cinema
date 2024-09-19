import time
from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        db_connection = None
        while not db_connection:
            try:
                db_connection = connections["default"]
                self.stdout.write(self.style.SUCCESS("Connected to database"))
            except OperationalError:
                self.stdout.write(self.style.ERROR(
                    "Database unavailable, wait 1 second..."))
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("Database available!"))
