import time
from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Waiting for db...")

        db_ready = False
        while not db_ready:
            try:
                connections["default"].cursor()
                db_ready = True
            except OperationalError:
                self.stdout.write("Database unavailable, waiting...")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("Database available"))
