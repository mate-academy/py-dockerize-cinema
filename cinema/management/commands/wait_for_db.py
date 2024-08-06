from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError
import time


class Command(BaseCommand):
    help = "Checks if the database is ready for connections."  # noqa VNE003

    def handle(self, *args, **kwargs):
        db_conn = connections["default"]
        max_retries = 5
        for i in range(max_retries):
            try:
                db_conn.cursor()
                self.stdout.write(self.style.SUCCESS("Database is ready!"))
                return
            except OperationalError:
                self.stdout.write(
                    f"Database not ready, retrying {i + 1}/{max_retries}..."
                )
                time.sleep(2)
        self.stdout.write(self.style.ERROR(
            "Database not ready after maximum retries."
        ))
