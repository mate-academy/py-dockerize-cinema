import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    hel = ("Wait for the database to "
            "be available before running other commands")

    def handle(self, *args, **kwargs):
        self.stdout.write("Waiting for database...\n")
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections["default"]
                self.stdout.write(self.style.SUCCESS("Database available!"))
            except OperationalError:
                self.stdout.write("Database unavailable, "
                                  "waiting 1 second...\n")
                time.sleep(1)
