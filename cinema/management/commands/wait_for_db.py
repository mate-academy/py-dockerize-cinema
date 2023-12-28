import time
from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    desc = "Wait for the database to be available"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Waiting for database..."))
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections["default"]
            except OperationalError:
                self.stdout.write(
                    self.style.WARNING(
                        "Database unavailable, waiting 2 seconds..."
                    )
                )
                time.sleep(2)

        self.stdout.write(
            self.style.SUCCESS("Database is available!")
        )
