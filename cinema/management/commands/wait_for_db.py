import time

from django.core.management.base import BaseCommand, CommandError
from psycopg2 import OperationalError
from django.db import connections


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        db_connection = None
        while not db_connection:
            try:
                db_connection = connections["default"]
            except OperationalError:
                raise CommandError("Database unavailable,waiting 1 seconds")
            time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available!"))
