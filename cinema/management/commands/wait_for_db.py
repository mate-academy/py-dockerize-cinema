from django.core.management.base import BaseCommand, CommandError
from django.db import connections
from django.db.utils import OperationalError
import time


class Command(BaseCommand):
    help = "Waits for the database to become available."  # noqa VNE003

    def add_arguments(self, parser):
        parser.add_argument(
            "--timeout",
            type=int,
            default=60,
            help="Maximum time (in seconds) to wait for the database."
        )

    def handle(self, *args, **options):
        timeout = options.get("timeout")
        self.stdout.write("Waiting for database connection...")
        start_time = time.time()
        while True:
            try:
                connections["default"].cursor()
                break
            except OperationalError:
                elapsed = time.time() - start_time
                if timeout and elapsed > timeout:
                    raise CommandError(
                        f"Database connection timed out "
                        f"after {timeout} seconds."
                    )
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("Database available!"))
