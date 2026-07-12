import time
from django.core.management.base import BaseCommand, CommandError
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    """Django command to pause execution until
    the database is available with a timeout."""

    def add_arguments(self, parser):
        # Correct method name is add_arguments (plural)
        parser.add_argument(
            "--timeout",
            type=int,
            default=60,
            help="Max seconds to wait for DB"
        )

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")

        start_time = time.time()
        timeout = options["timeout"]
        db_conn = None

        while not db_conn:
            # Calculate elapsed time
            elapsed = time.time() - start_time
            if elapsed > timeout:
                raise CommandError(
                    f"Database timeout reached after {timeout} seconds."
                )

            try:
                db_conn = connections["default"]
                # Perform a simple check to ensure the connection is active
                db_conn.cursor()
            except OperationalError:
                db_conn = None
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available!"))
