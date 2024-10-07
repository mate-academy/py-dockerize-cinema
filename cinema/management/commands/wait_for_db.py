from django.core.management.base import BaseCommand
import time
from psycopg import OperationalError
from django.db import connections


class Command(BaseCommand):
    help = "Wait for the database to be available."  # noqa

    def handle(self, *args, **kwargs):
        db_conn = connections["default"]
        while not db_conn:
            try:
                db_conn.ensure_connection()
            except OperationalError:
                self.stdout.write(
                    self.style.ERROR(
                        "Database unavailable, waiting 1 second..."
                    )
                )
                time.sleep(1)
