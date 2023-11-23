import time

from django.core.management import BaseCommand
from django.db.utils import OperationalError
from django.db import connections


class Command(BaseCommand):
    """Pauses execution until db is available"""

    def handle(self, *args, **options):
        db_connect = None
        while not db_connect:
            try:
                db_connect = connections["default"].cursor()
            except OperationalError:
                self.stdout.write(
                    self.style.WARNING(
                        "Database unavailable, waiting 1 second..."
                    )
                )
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("Database available"))
