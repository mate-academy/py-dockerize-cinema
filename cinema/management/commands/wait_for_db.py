import time

from django.core.management import BaseCommand
from django.db import connections, OperationalError


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        self.stdout.write("Waiting for db to stand up")
        db_connection = None
        while not db_connection:
            try:
                db_connection = connections["default"].ensure_connection()
                break
            except OperationalError:
                self.stdout.write(self.style.WARNING("Something went wrong"))
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("Connected!"))
