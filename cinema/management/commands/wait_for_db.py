import time

from django.core.management.base import BaseCommand
from django.db.utils import OperationalError
from psycopg import OperationalError as PsycopgOperationalError


class Command(BaseCommand):
    help = "Force the app to wait while the database is unavailable"

    def handle(self, *args, **options) -> None:
        self.stdout.write("Waiting for the database...")
        db_up = False

        while not db_up:
            try:
                self.check(databases=("default",))
                db_up = True
            except (PsycopgOperationalError, OperationalError):
                self.stdout.write(
                    "Database is unavailable, wait for a second..."
                )
                time.sleep(1)

        self.stdout.write(
            self.style.SUCCESS("The database is available!")
        )
