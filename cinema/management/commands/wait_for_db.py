import os
import time

from django.core.management.base import (
    BaseCommand,
    CommandParser,
    DjangoHelpFormatter
)
from django.db import OperationalError
from django.db import connection

WAITING = 1


class Command(BaseCommand):
    help = "Waits for the database to be available"

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        db_conn = None
        while not db_conn:
            try:
                connection.ensure_connection()
                db_conn = True
            except OperationalError:
                self.stdout.write(f"Database unavailable, waiting"
                                  f" {WAITING} second...")
                time.sleep(WAITING)
