import time

from django.core.management import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        self.stdout.write("Waiting for database...")
        connection_to_db = None

        while not connection_to_db:
            try:
                connection_to_db = connections["default"]
            except OperationalError:
                self.stdout.write("Database unavailable, waiting 2 second...")
                time.sleep(2)
            self.stdout.write(self.style.SUCCESS("Database available"))
