import time

from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    help = "Wait until the database is available"

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        while True:
            try:
                connections["default"].ensure_connection()
            except OperationalError:
                time.sleep(1)
            else:
                self.stdout.write(self.style.SUCCESS("Database is available"))
                return
