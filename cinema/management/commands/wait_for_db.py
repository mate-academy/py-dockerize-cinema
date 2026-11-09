import time

from django.core.management import BaseCommand
from django.db import connection
from django.db.utils import OperationalError


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Waiting for db connection...")

        db_conn = False
        while not db_conn:
            try:
                connection.ensure_connection()
                db_conn = True
            except OperationalError:
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)
        return "Database available"
