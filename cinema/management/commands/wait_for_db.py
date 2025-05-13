import time
from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Command for waiting database"""

    def handle(self, *args, **options):
        self.stdout.write("Waiting for db...")
        db_up = False
        while not db_up:
            try:
                self.check(databases=["default"])
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write(
                    "Connecting to data base failed, wait to reconnect..."
                )
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Data base available!"))
