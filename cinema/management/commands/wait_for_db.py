import time

from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    """Additional command to wait for database"""

    def handle(self, *args, **options):
        self.stdout.write("Wait for database...")
        db = None
        while not db:
            try:
                db = connections["default"].cursor()
            except OperationalError:
                self.stdout.write("Database is not connected...")
                time.sleep(1)

        self.stdout.write("Database is connected")
