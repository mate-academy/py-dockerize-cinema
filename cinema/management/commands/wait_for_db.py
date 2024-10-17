import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        db_connection = None
        while not db_connection:
            try:
                db_connection = connections["default"]
                db_connection.ensure_connection()
                self.stdout.write("Connecting to database.")
            except OperationalError:
                self.stdout.write("Database unavailable.")
                time.sleep(2)
            except Exception as e:
                self.stdout.write(f"An error occurred: {str(e)}")
                time.sleep(2)
            else:
                self.stdout.write("Database available.")
