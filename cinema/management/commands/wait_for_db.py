from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError
import time


class Command(BaseCommand):
    command_help = "Waits for the database to be available before continuing"

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")

        while True:
            try:
                connections["default"].ensure_connection()
                with connections["default"].cursor() as cursor:
                    cursor.execute("SELECT 1")
                self.stdout.write(self.style.SUCCESS("Database is ready!"))
                break
            except OperationalError:
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)
