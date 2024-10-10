import time

from django.core.management.base import BaseCommand
from django.db import connection
from django.db.utils import OperationalError


class Command(BaseCommand):
    times = 10
    def handle(self, *args, **options):
        for attempt in range(self.times):
            try:
                connection.ensure_connection()
            except OperationalError:
                self.stdout.write(f"Attempt: {attempt + 1} / {self.times}")
                time.sleep(5)
            else:
                self.stdout.write(self.style.SUCCESS("Database found!"))
                return

        self.stdout.write(self.style.ERROR("Failed to find database."))
