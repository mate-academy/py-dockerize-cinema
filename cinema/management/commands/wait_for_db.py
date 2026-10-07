from django.core.management.base import BaseCommand
from django.db import connection
from time import sleep
import sys


class Command(BaseCommand):
    help = "Waits for db to become available"

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database. . .")

        db_ready = False
        attempts = 0
        max_attempts = 10

        while not db_ready and attempts <= max_attempts:
            try:
                connection.ensure_connection()
                db_ready = True
                self.stdout.write("Database is ready!")

            except Exception:
                self.stdout.write("Waiting. . .")
                sleep(1)
                attempts += 1

        if not db_ready:
            self.stdout.write(
                self.style.ERROR(
                    "Database not available."
                )
            )

            sys.exit()
