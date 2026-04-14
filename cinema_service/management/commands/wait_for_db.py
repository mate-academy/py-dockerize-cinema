import time

from django.core.management.base import BaseCommand
from django.db import connection
from django.db.utils import OperationalError


class Command(BaseCommand):
    def handle(self, *args, **options):
        while True:
            try:
                self.stdout.write("Waiting for database...")
                connection.ensure_connection()
                self.stdout.write("Database available!")
                break
            except OperationalError:
                time.sleep(3)
