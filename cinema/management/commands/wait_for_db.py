import time

from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError

#  Command, which waits for the database to be available


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Waiting for database connection...")
        db_connect = None
        while not db_connect:
            try:
                db_connect = connections["default"].cursor()
            except OperationalError:
                self.stdout.write(self.style.ERROR(
                    "Database unavailable, waiting for 3 seconds..."))
                time.sleep(3)
        self.stdout.write(self.style.SUCCESS("Database connected!"))
