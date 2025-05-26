import time
from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError
from typing import Any


class Command(BaseCommand):
    help = "Waits for database to be available"  # noqa: VNE003

    def handle(self, *args: str, **options: Any) -> None:
        self.stdout.write("Waiting for database…")
        db_conn = connections["default"]
        while True:
            try:
                db_conn.cursor()
                break
            except OperationalError:
                self.stdout.write(
                    "Database unavailable, sleeping 1 second…"
                )
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("Database available!"))
