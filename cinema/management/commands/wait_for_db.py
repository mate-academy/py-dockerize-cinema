import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Wait for database to be available"

    def handle(self, *args, **options) -> None:
        self.stdout.write("Waiting for database...")
        db_conn = None
        while True:
            try:
                db_conn = connections["default"]
                c = db_conn.cursor()
                self.stdout.write(self.style.SUCCESS("Database available!"))
                break
            except OperationalError:
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)
