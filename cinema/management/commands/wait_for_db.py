import time

from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError
from psycopg import OperationalError as PsycopgOperationalError


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")

        database_connection = None

        while database_connection is None:
            try:
                database_connection = connections["default"]
                database_connection.ensure_connection()
            except (OperationalError, PsycopgOperationalError):
                self.stdout.write(
                    "Database unavailable, waiting 1 second..."
                )
                database_connection = None
                time.sleep(1)

            self.stdout.write(
                self.style.SUCCESS('Database available! "%s"')
            )
