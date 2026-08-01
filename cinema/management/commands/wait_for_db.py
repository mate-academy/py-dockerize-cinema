from datetime import time
from sqlite3 import OperationalError

from django.core.management import BaseCommand
from django.db import connections


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections["default"]
                db_conn.cursor()
            except OperationalError:
                self.stdout.write(
                    self.style.ERROR(
                        "Database unavailable, waiting 10 seconds..."
                    )
                )
                time.sleep(10)

            self.stdout.write(self.style.SUCCESS("Database available!"))
