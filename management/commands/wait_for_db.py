import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        self.stdout.write("Database connection")
        db_connection = None
        while not db_connection:
            try:
                db_connection = connections["default"]
                self.stdout.write(self.style.SUCCESS("Connect"))
            except OperationalError:
                self.stdout.write("Error, retry after 3 seconds")
                time.sleep(3)
