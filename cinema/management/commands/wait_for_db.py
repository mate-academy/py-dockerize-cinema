import time
from django.core.management.base import BaseCommand
from django.db.utils import OperationalError
from django.db import connections


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Waiting for the database...")
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections["default"]
                db_conn.cursor()
            except OperationalError:
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available!"))
