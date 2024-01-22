import time

from django.core.management import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    help = "Script to wait for database before app runs"

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS("Waiting for database...")
        )
        db_connection = None

        while not db_connection:
            try:
                db_connection = connections["default"]
            except OperationalError:
                self.stdout.write(
                    self.style.WARNING(
                        "Database is not available. Next try in 5 seconds."
                    )
                )
                time.sleep(5)

        self.stdout.write(
            self.style.SUCCESS("Database is available! Continuing...")
        )
