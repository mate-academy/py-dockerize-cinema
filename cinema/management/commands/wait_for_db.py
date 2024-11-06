import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Waits for database to be ready before proceeding."

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        db_conn = None
        attempts = 0
        while not db_conn:
            try:
                db_conn = connections["default"]

                db_conn.ensure_connection()
                self.stdout.write(self.style.SUCCESS("Connected to database."))
            except OperationalError:
                attempts += 1
                if attempts > 5:
                    raise CommandError(
                        "Database connection failed after 5 attempts."
                    )
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)
