import time
from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    """Django command to wait for database to be available."""

    def handle(self, *args, **options):
        """Handle the command."""
        self.stdout.write("Waiting for database...")
        db_conn = None
        max_retries = 10
        retry_delay = 1

        for i in range(max_retries):
            try:
                db_conn = connections["default"]
                db_conn.ensure_connection()
                self.stdout.write(self.style.SUCCESS("Database is available!"))
                return
            except OperationalError as e:
                if i < max_retries - 1:
                    self.stdout.write(
                        f"Database unavailable, waiting "
                        f"{retry_delay} second(s)..."
                    )
                    time.sleep(retry_delay)
                    retry_delay *= 2
                else:
                    self.stdout.write(
                        self.style.ERROR(f"Could not connect to database: {e}")
                    )
                    raise
