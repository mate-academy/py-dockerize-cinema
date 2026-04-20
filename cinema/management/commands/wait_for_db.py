import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        attempts = 0
        max_attempts = 20

        while attempts < max_attempts:
            try:
                db_conn = connections["default"]
                db_conn.cursor()
                self.stdout.write(self.style.SUCCESS(
                    f"Database available after {attempts + 1} attempt(s)!"
                ))
                return
            except OperationalError:
                attempts += 1
                self.stdout.write(
                    f"Database unavailable "
                    f"(attempt {attempts}/{max_attempts}), waiting 1s..."
                )
                time.sleep(1)

        raise CommandError("Database unavailable after maximum attempts.")
