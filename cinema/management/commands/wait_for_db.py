import time

from django.core.management import BaseCommand
from django.db import OperationalError
from psycopg import OperationalError as PsycopgOpError


class Command(BaseCommand):
    """Waits for the database to be available"""

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=["default"])
                db_up = True
            except (PsycopgOpError, OperationalError):
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available!"))
