import time
from django.core.management.base import BaseCommand
from django.db import connection
from django.db.utils import OperationalError


class Command(BaseCommand):
    def handle(self, *args, **options):
        while True:
            try:
                connection.ensure_connection()
                self.stdout.write(self.style.SUCCESS("Database is available"))
                return
            except OperationalError:
                self.stdout.write("Waiting for database...")
                time.sleep(1)
