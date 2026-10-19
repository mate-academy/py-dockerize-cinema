import time

from django.core.management.base import BaseCommand, CommandError
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    info = "Waits for the database to become available"

    def add_arguments(self, parser):
        parser.add_argument(
            "--timeout",
            type=int,
            default=60,
            help="Max seconds to wait (default: 60)",
        )

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        timeout = options["timeout"]
        start = time.monotonic()

        while True:
            try:
                connections["default"].ensure_connection()
            except OperationalError as error:
                if time.monotonic() - start > timeout:
                    raise CommandError(
                        f"Database unavailable after {timeout} seconds"
                    ) from error
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)
            else:
                self.stdout.write(self.style.SUCCESS("Database available!"))
                return
