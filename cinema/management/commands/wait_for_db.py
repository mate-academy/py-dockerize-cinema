import time
from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        db_conn = None

        while True:
            try:
                db_conn = connections["default"]
                db_conn.cursor()
                break
            except OperationalError:
                self.stdout.write("Database unavailable, waiting...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available"))
