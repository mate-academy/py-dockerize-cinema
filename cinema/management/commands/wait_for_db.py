import time

from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):

    def handle(self, *args, **options):
        retry_delay = 5
        self.stdout.write("waiting for db")
        db_conn = None

        while not db_conn:
            try:
                db_conn = connections["default"].cursor()
                self.stdout.write(self.style.SUCCESS("Database is available"))
            except OperationalError:
                self.stdout.write("Database is not available. Retrying...")
                time.sleep(retry_delay)
        self.stdout.write(self.style.ERROR(
            "Unable to connect to the database"
        ))
