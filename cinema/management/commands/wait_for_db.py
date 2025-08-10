import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        while True:
            try:
                db_conn = connections["default"]
                db_conn.cursor()  # якщо БД не готова — буде OperationalError
                self.stdout.write(self.style.SUCCESS("Database available!"))
                break
            except OperationalError:
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)
