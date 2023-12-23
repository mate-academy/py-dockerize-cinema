from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError
import time


class Command(BaseCommand):
    help = "Waits for the database to become available"

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        db_conn = None
        while not db_conn:
            try:
                db_connection = connections["default"]
                db_connection.ensure_connection()
                db_conn = True
            except OperationalError:
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available!"))
