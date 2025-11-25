import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        db_connection = None
        while not db_connection:
            try:
                db_connection = connections["default"]
                db_connection.cursor()
            except OperationalError:
                self.stdout.write("Database connection, waiting 1 second...")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("Database connection."))
