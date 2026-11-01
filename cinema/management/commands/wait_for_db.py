import time

from django.core.management.base import BaseCommand
from django.db.utils import OperationalError
from psycopg2 import OperationalError as Psycopg2OperationalError
from django.db import connections


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")

        db_connection = None

        while db_connection is None:
            try:
                db_connection = connections["default"]
                db_connection.cursor()
            except (OperationalError, Psycopg2OperationalError):
                self.stdout.write(
                    "Database is not ready, waiting for 1 second..."
                )
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database is available!"))
