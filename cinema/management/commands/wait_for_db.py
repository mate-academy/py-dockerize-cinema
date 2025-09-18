import time

from django.core.management import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    helps = "Waits until database is available"

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")

        db_ready = False
        while not db_ready:
            try:
                conn = connections["default"]
                conn.cursor()
                db_ready = True
            except OperationalError:
                self.stdout.write("Database unavailable, waiting 1s...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available!"))
