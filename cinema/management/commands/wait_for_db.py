from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError
import time


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        self.stdout.write("Waiting for database ...")
        db_conn = None

        while not db_conn:
            try:
                db_conn = connections["default"]
                self.stdout.write(
                    self.style.SUCCESS("Database available")
                )
            except OperationalError:
                self.stdout.write(
                    "Database unavailable, please wait ..."
                )
                time.sleep(1)
