from django.core.management.base import BaseCommand
from django.db import connections, OperationalError
from psycopg2 import OperationalError as PsycopgError
import time


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Check database connection...")
        database_connection = None
        while not database_connection:
            try:
                database_connection = connections["default"].cursor()
            except (OperationalError, PsycopgError):
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("Database connected!"))
