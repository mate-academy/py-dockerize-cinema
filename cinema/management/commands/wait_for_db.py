import time
from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    help = "Wait for DB"  # noqa: VNE003

    def handle(self, *args, **options):
        self.stdout.write("Wait for DB...")
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections["default"]
                db_conn.ensure_connection()
            except OperationalError:
                self.stdout.write("DB not available, wait 1 sec.")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("DB available!"))
