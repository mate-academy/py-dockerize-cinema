import time

from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    help = "Wait until the database is available"  # noqa: VNE003

    def add_arguments(self, parser):
        parser.add_argument(
            "--timeout",
            type=int,
            default=60,
            help="Max seconds to wait before giving up (default: 60)",
        )

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        deadline = time.monotonic() + options["timeout"]

        while True:
            try:
                connections["default"].ensure_connection()
                break
            except OperationalError:
                if time.monotonic() >= deadline:
                    raise
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available!"))
