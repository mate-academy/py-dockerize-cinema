from django.core.management.base import BaseCommand, no_translations
from django.db import connections
from django.db.utils import OperationalError

import time


class Command(BaseCommand):
    @no_translations
    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Waiting for database..."))
        db_conn = None

        while not db_conn:
            try:
                db_conn = connections["default"]
            except OperationalError:
                self.stdout.write(
                    self.style.ERROR(
                        "Database is not available, waiting..."
                    )
                )
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available!"))
