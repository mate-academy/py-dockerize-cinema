import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help_text = "Waits until database is available"

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        db_up = False
        while not db_up:
            try:
                connections["default"].ensure_connection()
                db_up = True
            except OperationalError:
                self.stdout.write("Waiting for database...")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("Database connected."))
