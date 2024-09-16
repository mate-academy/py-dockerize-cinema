"""
Django command to wait for the database to come up
"""

import time

from django.db import connections
from psycopg2 import OperationalError

from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write("Wait for database...")
        max_attempts = 10
        attempts = 0
        db_up = False
        while not db_up and attempts < max_attempts:
            try:
                connections["default"].ensure_connection()
                db_up = True
            except OperationalError as e:
                attempts += 1
                self.stdout.write(f"Attempt {attempts}/{max_attempts}: {e}")
                time.sleep(1)

        if db_up:
            self.stdout.write(self.style.SUCCESS("Database available"))
        else:
            self.stdout.write(self.style.ERROR(
                "Unable to connect to the database."
            ))
