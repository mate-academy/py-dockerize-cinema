import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        self.stdout.write("Waiting for database...")
        db_conn = None

        while not db_conn:
            try:
                db_conn = connections["default"]
            except OperationalError:
                self.stdout.write("Database unavailable, waiting 5 second...")
                time.sleep(5)

        self.stdout.write(self.style.SUCCESS("Database available!"))
