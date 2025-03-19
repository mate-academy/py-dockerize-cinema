import time

from django.core.management.base import BaseCommand
from django.db import connections, OperationalError


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Waiting for database connection..")
        db_connection = None
        while db_connection is None:
            try:
                db_connection = connections["default"]
            except OperationalError:
                self.stdout.write("Database is not ready..")
                time.sleep(1)

        self.stdout.write(
            self.style.SUCCESS("Database connection established")
        )
