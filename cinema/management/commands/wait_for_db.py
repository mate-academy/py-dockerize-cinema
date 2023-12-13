import time

from django.core.management import BaseCommand
from django.db.utils import OperationalError
from django.db import connections


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Connecting to the database...")

        connection = None

        while not connection:
            try:
                connection = connections["default"]
            except OperationalError:
                self.stdout.write("...")
                time.sleep(1)

        self.stdout.write(
            self.style.SUCCESS("Database was connected!")
        )