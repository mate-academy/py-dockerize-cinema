import time

from django.core.management.base import BaseCommand
from django.db import OperationalError, connection


class Command(BaseCommand):
    help = "Wait until the default database is available."  # noqa: VNE003

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        while True:
            try:
                connection.ensure_connection()
            except OperationalError:
                time.sleep(1)
            else:
                break
        self.stdout.write(self.style.SUCCESS("Database available!"))
