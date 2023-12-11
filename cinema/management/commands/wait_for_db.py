import time

from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        self.stdout.write("Waiting for connection to database...")
        db_connection = None
        while not db_connection:
            try:
                db_connection = connections["default"]
            except OperationalError:
                self.stdout.write("Database not connected, waiting...")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS(
            "Database system is ready to accept connections"
        ))
