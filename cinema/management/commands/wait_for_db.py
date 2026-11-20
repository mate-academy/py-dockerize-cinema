import time

from django.core.management.base import BaseCommand, no_translations
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    @no_translations
    def handle(self, *args, **options) -> None:
        self.stdout.write("Waiting for database...")
        db_conn = None
        while db_conn is None:
            try:
                db_conn = connections["default"]
                db_conn.cursor()
            except OperationalError:
                self.stdout.write(
                    "Database unavailable, waiting 1 second..."
                )
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("Database available!"))
