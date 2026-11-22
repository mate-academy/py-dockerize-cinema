import time

from django.core.management.base import BaseCommand, CommandError
from django.db import connection, OperationalError


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--timeout",
            type=int,
            default=60,
            help="Maximum time to wait for database in seconds",
        )

    def handle(self, *args, **options):
        timeout = options["timeout"]
        start = time.monotonic()
        self.stdout.write("Waiting for database...")
        while True:
            try:
                connection.ensure_connection()
                break
            except OperationalError:
                self.stdout.write("Database unavailable")
                if time.monotonic() - start >= timeout:
                    raise CommandError(
                        f"Database unavailable after {timeout} seconds"
                    )
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("Database available!"))
