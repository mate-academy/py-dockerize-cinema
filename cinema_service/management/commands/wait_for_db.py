import time

from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        self.stdout.write("Waiting for database...")
        db_conn = None
        while db_conn is None:
            try:
                db_conn = connections["default"]
                db_conn.cursor()
            except OperationalError:
                self.stdout.write(
                    "Database unavailable, waiting 3 seconds..."
                )
                time.sleep(3)
        self.stdout.write(self.style.SUCCESS("Database connected!"))
