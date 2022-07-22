import time
from django.db import connections as connect
from django.db.utils import OperationalError
from django.core.management import BaseCommand


class Command(BaseCommand):
    """Wait while DB will be ready"""

    def handle(self, *args, **options):
        print('Waiting for DB', end="")
        db_connection = None
        while not db_connection:
            try:
                db_connection = connect["default"]
            except OperationalError:
                print(".", end="")
                time.sleep(1)
