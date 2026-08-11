import time

from django.core.management.base import BaseCommand
from django.db import connection
from django.db.utils import OperationalError


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        max_retries = 30
        retries = 0

        while retries < max_retries:
            try:
                connection.ensure_connection()
            except OperationalError:
                retries += 1
                self.stdout.write(
                    f"Database unavailable, waiting..."
                    f" ({retries}/{max_retries})"
                )
                time.sleep(1)
            else:
                self.stdout.write(self.style.SUCCESS("Database available!"))
                break
        else:
            self.stdout.write("Database not available after timeout")
            return
