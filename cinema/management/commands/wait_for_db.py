import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        db_conn = None
        while db_conn is None:
            try:
                db_conn = connections["default"]
                cursor = db_conn.cursor()
                cursor.close()
            except OperationalError:
                self.stdout.write("Database unavailable, waiting...")
                db_conn = None
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("Database available!"))
