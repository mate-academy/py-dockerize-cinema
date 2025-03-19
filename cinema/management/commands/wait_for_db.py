import time

from django.core.management.base import BaseCommand
from django.db import connection, OperationalError


class Command(BaseCommand):
    def handle(self, *args, **options):
        is_connected = False
        for _ in range(20):  # Waits for 20 seconds.
            try:
                connection.ensure_connection()
                is_connected = True
                break
            except OperationalError:
                self.stdout.write("Waiting for database...")
                time.sleep(1)
        if is_connected:
            self.stdout.write(self.style.SUCCESS("Connected!"))
        else:
            raise OperationalError("Database not available!")
