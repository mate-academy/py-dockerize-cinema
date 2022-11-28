import time

from django.core.management import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Opening the DB.")
        connection = None

        while not connection:
            try:
                connection = connections["default"]
            except OperationalError:
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Successfully opened the DB!"))
