import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to pause execution until the database is available."""

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        db_conn = None
        attempts = 0
        max_attempts = 30
        wait_time = 1

        while not db_conn:
            try:
                db_conn = connections["default"]
                db_conn.cursor()
            except OperationalError:
                attempts += 1
                if attempts >= max_attempts:
                    self.stdout.write(
                        self.style.ERROR(
                            "Database unavailable after maximum attempts. "
                            "Exiting..."
                        )
                    )
                    self.stderr.write(
                        "Maximum attempts reached. "
                        "Could not connect to the database."
                    )
                    return

                self.stdout.write(
                    f"Database unavailable, waiting {wait_time} second(s)... "
                    f"(Attempt {attempts}/{max_attempts})"
                )
                time.sleep(wait_time)

        self.stdout.write(self.style.SUCCESS("Database available!"))
