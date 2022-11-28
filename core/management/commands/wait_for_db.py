from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError
import time


class Command(BaseCommand):
    """Django command to pause execution until database is available"""

    def handle(self, *args, **kwargs):
        self.stdout.write("Waiting for db...")
        db_cur = None
        while not db_cur:
            try:
                db_cur = connections["default"].cursor()
                self.stdout.write(self.style.SUCCESS("DB available!"))
            except OperationalError:
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)
