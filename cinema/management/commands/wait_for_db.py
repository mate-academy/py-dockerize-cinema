import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management import BaseCommand


class Command(BaseCommand):
    """Django command to suspend execution until the database is available"""

    def handle(self, *args, **options) -> None:
        self.stdout.write("Waiting for database...")
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections["default"]
            except OperationalError:
                self.stdout.write("Database is still connecting...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available!"))
