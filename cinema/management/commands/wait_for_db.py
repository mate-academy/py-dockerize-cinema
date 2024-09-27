import time

from django.core.management import BaseCommand
from django.db.utils import OperationalError
from django.db import connections


class Command(BaseCommand):
    """Pauses execution until db is available"""

    def handle(self, *args, **options):
        max_attempts = 10
        attempt_count = 0

        while attempt_count < max_attempts:
            try:
                _ = connections["default"].cursor()
                self.stdout.write(self.style.SUCCESS(
                    "Database available, Lesha"
                ))
                return
            except OperationalError:
                attempt_count += 1
                self.stdout.write(
                    self.style.WARNING(
                        f"Database unavailable, waiting 1 second... "
                        f"(Attempt {attempt_count}/{max_attempts})"
                    )
                )
                time.sleep(1)

        self.stdout.write(self.style.ERROR(
            "All attempts failed. Exiting."))
