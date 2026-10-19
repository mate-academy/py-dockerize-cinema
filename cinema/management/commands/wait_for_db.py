import time

from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    help = "Wait for db connection"  # noqa: VNE003

    def handle(self, *args, **options):
        self.stdout.write("Wait for db connection...")

        while True:
            try:
                connections["default"].ensure_connection()
                break
            except OperationalError:
                self.stdout.write("Database unavailable, waiting again...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available!"))
