import sys
from django.db import OperationalError

from django.db import connections
from django.core.management.base import BaseCommand
import time


class Command(BaseCommand):
    def handle(self, *args, **options):
        for attempt in range(10):
            try:
                connections["default"].cursor()
                self.stdout.write(
                    self.style.SUCCESS(
                        "Database connection established"
                    )
                )
                return

            except OperationalError:
                self.stdout.write(
                    self.style.ERROR(
                        "Database connection failed"
                    )
                )
                time.sleep(3)

        sys.exit(1)
