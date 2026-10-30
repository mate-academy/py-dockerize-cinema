import sys
import time
from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        max_retries = 50
        retries = 0
        try:
            while retries < max_retries:
                try:
                    db_conn = connections["default"]
                    db_conn.cursor()
                    self.stdout.write(self.style.SUCCESS(
                        "Database available!"
                    ))
                    return
                except OperationalError:
                    retries += 1
                    self.stdout.write(
                        "Database unavailable, wait 1 second..."
                    )
                    time.sleep(1)

            self.stdout.write(self.style.ERROR(
                "Database not available after max retries, exiting."
            ))
            sys.exit(1)

        except KeyboardInterrupt:
            self.stdout.write(self.style.ERROR(
                "Interrupted by user, exiting."
            ))
            sys.exit(1)
