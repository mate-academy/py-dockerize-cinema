import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to pause execution until database is available"""

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        db_conn = None
        start_time = time.time()

        while not db_conn:
            try:
                db_conn = connections["default"]
            except OperationalError:
                if time.time() - start_time > 10:
                    self.stdout.write(
                        self.style.ERROR(
                            "Database not available after "
                            "10 seconds, exiting..."
                        )
                    )
                    raise OperationalError(
                        "Database not available within timeout period."
                    )
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available!"))
