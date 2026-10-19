import time

from django.core.management import CommandParser
from django.core.management.base import BaseCommand, CommandError
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        timeout = options["timeout"]
        start = time.monotonic()
        while True:
            try:
                connections["default"].ensure_connection()
            except OperationalError:
                self.stdout.write(self.style.WARNING("Still in progress..."))
                time.sleep(1)
            else:
                break
            if time.monotonic() - start > timeout:
                raise CommandError(
                    f"Database unavailable after {timeout} seconds"
                )
        self.stdout.write(self.style.SUCCESS("Database available!"))

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "--timeout",
            type=int,
            default=30,
            help="Timeout value for database waiting"
        )
