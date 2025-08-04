import time
from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    """Django command to wait for database to be available"""

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")

        start_time = time.time()

        db_conn = None
        attempt = 1

        while not db_conn:
            try:
                db_conn = connections["default"]
                db_conn.ensure_connection()
            except OperationalError:
                elapsed_time = time.time() - start_time
                self.stdout.write(
                    f"Database unavailable ("
                    f"attempt {attempt}, {elapsed_time:.1f}s elapsed), "
                    f"waiting 1 second..."
                )
                time.sleep(1)
                attempt += 1

        total_time = time.time() - start_time

        self.stdout.write(
            self.style.SUCCESS(
                f"Database available! Connected in {total_time:.2f} seconds "
                f"(after {attempt} attempts)"
            )
        )
