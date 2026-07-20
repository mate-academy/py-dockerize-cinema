import time

from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import InterfaceError, OperationalError


class Command(BaseCommand):
    help = "Wait for the database to become available."  # noqa: VNE003

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")

        db_available = False
        while not db_available:
            try:
                connections["default"].ensure_connection()
                db_available = True
            except (InterfaceError, OperationalError):
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available!"))
