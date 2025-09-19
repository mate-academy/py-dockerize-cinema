import time
from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError, DatabaseError

try:
    import psycopg2
    from psycopg2 import OperationalError as Psycopg2OpError
except ImportError:
    Psycopg2OpError = None


class Command(BaseCommand):
    """The command to wait for db connections"""

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections["default"]
                db_conn.cursor()
            except (OperationalError, DatabaseError) as e:
                if Psycopg2OpError and isinstance(e, Psycopg2OpError):
                    pass
                self.stdout.write(self.style.WARNING(
                    "Database unavailable, wait 1 second..."
                ))
                time.sleep(1)
            else:
                self.stdout.write(self.style.SUCCESS("Database available!"))
