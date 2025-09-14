import time as t
from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    help_text = "Wait for the database to become available"

    def handle(self, *args, **kwargs):
        self.stdout.write("⏳ Waiting for database...")
        while True:
            try:
                db_conn = connections["default"]
                db_conn.cursor()
                break
            except OperationalError:
                self.stdout.write("Database unavailable, sleeping 1s...")
                t.sleep(1)
        self.stdout.write(self.style.SUCCESS("✅ Database is available!"))
