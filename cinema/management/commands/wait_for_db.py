import time
from typing import Any

from django.core.management import BaseCommand
from django.db import OperationalError, connection


class Command(BaseCommand):
    help = "Waits for database connection"

    def handle(self, *args: Any, **options: Any) -> None:
        self.stdout.write("Waiting for database...")
        db_connection = False
        while not db_connection:
            try:
                connection.ensure_connection()
                db_connection = True
            except OperationalError:
                self.stdout.write(
                    self.style.WARNING(
                        "Cannot connect to database. Waiting 1 second..."
                    )
                )
                time.sleep(1)
        self.stdout.write(
            self.style.SUCCESS("Database connection has been established")
        )
