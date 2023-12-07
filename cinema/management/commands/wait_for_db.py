import time

from django.core.management import BaseCommand
from django.db import connection
from django.db.utils import OperationalError


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Wait for database...")
        db_connection = None
        while not db_connection:
            try:
                connection.ensure_connection()
                db_connection = True
            except OperationalError as e:
                self.stdout.write("Database not ready, waiting 1 sec...")
                print(e)
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("Database ready"))
