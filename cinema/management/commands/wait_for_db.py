import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        db_conn = None
        retries = 0
        max_retries = 30

        while not db_conn:
            try:
                db_conn = connections["default"]
                db_conn.cursor()
            except OperationalError:
                retries += 1
                if retries >= max_retries:
                    self.stderr.write(
                        "Database not available after max retries."
                    )
                    raise
                self.stdout.write(
                    f"Database unavailable, waiting 1 second... ("
                    f"{retries}/{max_retries}"
                    f")"
                )
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database is available!"))
