import time

from django.core.management.base import BaseCommand
from django.db import connection
from django.db.utils import OperationalError


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--times", type=int, default=10)

    def handle(self, *args, **options):
        times = options["times"]

        for attempt in range(times):
            try:
                connection.ensure_connection()
            except OperationalError:
                self.stdout.write(f"Attempt: {attempt + 1} / {times}")
                time.sleep(5)
            else:
                self.stdout.write(self.style.SUCCESS("Database found!"))
                return

        self.stdout.write(self.style.ERROR("Failed to find database."))
