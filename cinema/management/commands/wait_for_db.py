import time

from django.core.management import BaseCommand
from django.db import connections, OperationalError


class Command(BaseCommand):
    help = "Wait for database..."

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")

        db_conn = False
        while not db_conn:
            try:
                connections["default"].cursor()
                db_conn = True
            except OperationalError:
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("Database available!"))
