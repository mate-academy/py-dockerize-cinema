import time
from sqlite3 import OperationalError

from django.core.management import BaseCommand
from django.db import connections


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Waiting for database....")
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections["default"]
                db_conn.cursor()
            except OperationalError:
                self.stdout.write("Database unavailable, waiting 1 sec")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available"))
