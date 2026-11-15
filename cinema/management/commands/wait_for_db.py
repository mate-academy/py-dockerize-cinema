
import time

from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    help = "Wait for the database to become available"

    def handle(self, *args, **kwargs):
        self.stdout.write("Waiting for database...")

        db_connection = connections["default"]

        while True:
            try:
                db_connection.ensure_connection()
                break
            except OperationalError:
                self.stdout.write(
                    "Database unavailable, waiting..."
                )
                time.sleep(1)

        self.stdout.write(
            self.style.SUCCESS("Database available!")
        )
