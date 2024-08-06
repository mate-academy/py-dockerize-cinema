import time
from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    print("Wait for the database to become available")

    def handle(self, *args, **kwargs):
        self.stdout.write("Waiting for the database to become available...")

        db_conn = None
        while not db_conn:
            try:
                db_conn = connections["default"]
                db_conn.cursor()
            except OperationalError:
                self.stdout.write("Database not available, waiting...")
                time.sleep(1)
