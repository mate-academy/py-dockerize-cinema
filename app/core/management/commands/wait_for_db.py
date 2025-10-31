import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for database connection."""

    def handle(self, *args, **options):
        self.stdout.write("⏳ DB wake up. Wait for ...")
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections["default"]
                db_conn.cursor()
            except OperationalError:
                self.stdout.write("💤 DB sleep. Try it in one second...")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("✅ DB is success!"))
