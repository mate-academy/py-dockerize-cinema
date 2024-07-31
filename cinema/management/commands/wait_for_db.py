from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand
import time


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        db_up = False
        attempts = 0
        max_attempts = 60
        while not db_up and attempts < max_attempts:
            try:
                db_conn = connections["default"]
                db_conn.cursor()
                db_up = True
            except OperationalError:
                attempts += 1
                self.stdout.write(f"Database unavailable, waiting 1 second..."
                                  f"( attempt {attempts}/{max_attempts})")
                time.sleep(1)

        if db_up:
            self.stdout.write(self.style.SUCCESS("Database available!"))
        else:
            self.stdout.write(self.style.ERROR("Database not available after"
                                               " maximum attempts!"))
