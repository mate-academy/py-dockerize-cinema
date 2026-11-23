import time

from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    help = "Wait until the default database is available"  # noqa: VNE003

    def handle(self, *args, **options) -> None:
        self.stdout.write("Waiting for database...")
        db_conn = connections["default"]

        while True:
            try:
                db_conn.ensure_connection()
                break
            except OperationalError:
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available!"))
