import time

from django.core.management import BaseCommand
from django.db import connection, OperationalError


class Command(BaseCommand):
    """Command to wait for db to load"""

    def handle(self, *args, **options):
        db_connection = None
        while not db_connection:
            try:
                connection.ensure_connection()
                db_connection = True
            except OperationalError:
                print("Database is not connected. Waiting for 1 second...")
                time.sleep(1)
        print("Database has been connected.")
