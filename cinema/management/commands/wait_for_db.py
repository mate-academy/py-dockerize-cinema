import time

from django.core.management.base import BaseCommand
from django.db import OperationalError, connection


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        db_conn = None
        while not db_conn:
            try:
                connection.ensure_connection()
                db_conn = True
            except OperationalError:
                self.stdout.write("Database unavailable...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available!"))
