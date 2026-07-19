from django.core.management.base import BaseCommand
from django.db import OperationalError
from django.db.utils import OperationalError as DbOperationalError
import time


class Command(BaseCommand):
    command_help = "Wait for the database to be available"

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")

        db_up = False

        while not db_up:
            try:
                self.check(databases=["default"])
                db_up = True
            except (OperationalError, DbOperationalError):
                self.stdout.write(
                    "Database unavailable, waiting 1 second..."
                )
                time.sleep(1)

        self.stdout.write(
            self.style.SUCCESS("Database available!")
        )
