from time import sleep
from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        attempts = 10
        delay = 3

        for attempt in range(attempts):
            try:
                db_conn = connections["default"]
                db_conn.ensure_connection()
                self.stdout.write(self.style.SUCCESS("Database available!"))
                break
            except OperationalError:
                self.stdout.write(
                    f"Database unavailable, waiting {delay} second, "
                    f"and trying again... Attempt number {attempt + 1}"
                )
                sleep(delay)
