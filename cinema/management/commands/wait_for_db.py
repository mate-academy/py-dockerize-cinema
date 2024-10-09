import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        db_conn = None
        retry_delay = 1
        max_retries = 5
        retries = 0

        while not db_conn and retries < max_retries:
            try:
                db_conn = connections["default"]
            except OperationalError:
                retries += 1
                self.stdout.write(f"Database unavailable, retrying in"
                                  f" {retry_delay} seconds..."
                                  f" (attempt {retries}/{max_retries})")
                time.sleep(retry_delay)

        if db_conn:
            self.stdout.write(self.style.SUCCESS("Database available!"))
        else:
            self.stdout.write(
                self.style.ERROR(
                    "Database connection failed after several attempts."
                )
            )
