import time

from django.core.management.base import BaseCommand, CommandError
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("--timeout", type=int, default=30,
                            help="Seconds to wait before giving up")

    def handle(self, *args, **options):
        timeout = options["timeout"]
        start = time.monotonic()
        self.stdout.write("Waiting for database...")

        while True:
            try:
                connections["default"].ensure_connection()
                break
            except OperationalError:
                if time.monotonic() - start > timeout:
                    raise CommandError(
                        f"Database not available after {timeout}s"
                    )
                self.stdout.write("Not ready, retrying in 1s...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available"))
