import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management import BaseCommand


class Command(BaseCommand):
    """Stop execution until db is connected"""
    def handle(self, *args, **options):
        self.stdout.write("Waiting for database ...")

        db_conn = None
        while not db_conn:
            try:
                db_conn = connections["default"]
            except OperationalError:
                self.stdout.write(
                    "Database unavailable, waiting 1 sec ..."
                )
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS(
            "Database is available!!!!"
        ))
