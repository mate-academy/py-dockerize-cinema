import time
from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    description = "Waits for the database to be available."

    def handle(self, *args, **options):
        self.stdout.write("⏳ Waiting for database...")
        db_conn = None
        retries = 0

        while not db_conn:
            try:
                db_conn = connections["default"]
                db_conn.cursor()
            except OperationalError:
                retries += 1
                self.stdout.write(
                    self.style.WARNING(
                        f"⛔ DB unavailable, retrying... ({retries})"
                    )
                )
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("✅ Database is available!"))
