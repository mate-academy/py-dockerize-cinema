import time

from django.core.management.base import BaseCommand
from django.db import connection
from django.db.utils import OperationalError


class Command(BaseCommand):
    def handle(self, *args, **options):
        db_ready = False
        while not db_ready:
            try:
                self.stdout.write("Connecting to database...")
                connection.ensure_connection()
                db_ready = True
            except OperationalError:
                self.stdout.write(
                    "Connection attempt failed, retry in 1 second..."
                )
                time.sleep(1)
