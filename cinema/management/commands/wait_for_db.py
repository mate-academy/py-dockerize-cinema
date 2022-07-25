import time
from django.db import connections as connect
from django.db.utils import OperationalError
from django.core.management import BaseCommand


class Command(BaseCommand):
    """Wait while DB will be ready"""

    def handle(self, *args, **options):
        self.stdout.write("Checking DB ready", ending="")
        db_connection = connect["default"]
        while not db_connection:
            try:
                db_connection = connect["default"]
            except OperationalError:
                self.stdout.write(".", ending="")
                time.sleep(1)
        self.stdout.write("\nDB is ready!")
