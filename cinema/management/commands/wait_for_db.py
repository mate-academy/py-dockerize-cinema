import time
from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    help = "Waits for database to be available before continuing."

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        db_conn = None
        retries = 0
        max_retries = 10
        while not db_conn and retries < max_retries:
            try:
                db_conn = connections["default"]
                c = db_conn.cursor()
            except OperationalError:
                retries += 1
                self.stdout.write(
                    f"Database unavailable, waiting 1 second... (attempt {retries})"
                )
                time.sleep(1)
        if not db_conn:
            self.stderr.write(
                "Could not connect to database after several attempts."
            )
            exit(1)
        self.stdout.write(self.style.SUCCESS("Database available!"))
