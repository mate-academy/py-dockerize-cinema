import time
from django.db import connections
from django.core.management.base import BaseCommand
from django.db.utils import OperationalError


class Command(BaseCommand):
    """This command would wait for your db while u up your containers"""

    def handle(self, *args, **options) -> str | None:
        self.stdout.write("Waiting for database...")
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections["default"]
                db_conn.cursor()
            except OperationalError:
                self.stdout.write("Database not available yet, please wait...")
                time.sleep(0.1)

        self.stdout.write(self.style.SUCCESS("Database available!"))
