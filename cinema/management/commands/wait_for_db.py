import time

from django.core.management.base import BaseCommand
from django.db import connections, OperationalError


class Command(BaseCommand):
    help = "Waiting till database is available"

    def handle(self, *args, **kwargs):
        db_conn = None
        self.stdout.write("Waiting for db connection")
        while not db_conn:
            try:
                db_conn = connections["default"]
                db_conn.ensure_connection()
                self.stdout.write(self.style.SUCCESS("Database is available"))
            except OperationalError:
                self.stdout.write(
                    self.style.ERROR(
                        "Database is unavailable, retrying connection"
                    )
                )
                time.sleep(2)
