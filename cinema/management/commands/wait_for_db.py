from time import sleep
from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        db_conn = None
        attempts = 0

        while not db_conn:
            try:
                connections["default"].cursor()
                db_conn = connections["default"]
            except OperationalError:
                attempts += 1
                self.stdout.write(self.style.WARNING(
                    f"Database unavailable, waiting 1 second..."
                    f" (attempt {attempts})")
                )
                sleep(1)

        self.stdout.write(self.style.SUCCESS("Database is available!"))
