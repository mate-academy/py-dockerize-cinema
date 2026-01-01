import time

from django.core.management import BaseCommand
from django.db import connections, OperationalError


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Waiting for db connection...")

        db_conn = None
        while db_conn is None:
            try:
                db_conn = connections["default"]
                db_conn.cursor()
            except OperationalError:
                self.stdout.write(
                    self.style.WARNING("Database unavailable, trying again...")
                )
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database connected!"))
