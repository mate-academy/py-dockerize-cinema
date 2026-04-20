import time
from django.db.utils import OperationalError
from django.db import connections
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Waits for DB to be available"  # noqa: VNE003

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")

        while True:
            try:
                db_conn = connections["default"]
                db_conn.cursor()
            except OperationalError:
                self.stdout.write("Database unavailable, waiting 1 second")
                time.sleep(1)
            else:
                self.stdout.write(self.style.SUCCESS("Database available!"))
                break
