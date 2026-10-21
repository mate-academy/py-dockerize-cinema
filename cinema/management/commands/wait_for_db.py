import math
import time

from django.core.management.base import BaseCommand, CommandError
from django.db import connections
from django.db.utils import InterfaceError, OperationalError


class Command(BaseCommand):
    help = "Wait for the default database to accept queries."  # noqa: VNE003

    def add_arguments(self, parser):
        parser.add_argument("--timeout", type=float, default=60)
        parser.add_argument("--interval", type=float, default=1)

    def handle(self, *args, **options):
        timeout = options["timeout"]
        interval = options["interval"]
        if not all(
            math.isfinite(value) and value > 0
            for value in (timeout, interval)
        ):
            raise CommandError(
                "Timeout and interval must be positive and finite."
            )

        self.stdout.write("Waiting for database...")
        deadline = time.monotonic() + timeout
        connection = connections["default"]
        while True:
            try:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT 1")
            except (OperationalError, InterfaceError):
                connection.close()
                remaining = deadline - time.monotonic()
                if remaining <= 0:
                    raise CommandError(
                        "Database unavailable after waiting. "
                        "Check the database service and credentials."
                    ) from None
                self.stdout.write("Database unavailable, retrying...")
                time.sleep(min(interval, remaining))
            else:
                self.stdout.write(self.style.SUCCESS("Database available!"))
                return
