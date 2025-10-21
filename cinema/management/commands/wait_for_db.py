import time
from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    db_ready = "Waits for the database to be available"

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        connection_ready = False
        while not connection_ready:
            try:
                connections["default"].ensure_connection()
                connection_ready = True
            except OperationalError:
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("Database available!"))
