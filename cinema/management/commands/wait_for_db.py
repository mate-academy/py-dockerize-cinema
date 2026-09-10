from django.core.management.base import BaseCommand
from django.db import connection, OperationalError
import time


class Command(BaseCommand):
    def handle(self, *args, **options):
        while True:
            try:
                connection.ensure_connection()
                self.stdout.write(self.style.SUCCESS("Database available!"))
                break
            except OperationalError:
                time.sleep(1)
