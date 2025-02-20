import time

from django.core.management import BaseCommand
from django.db import connections, OperationalError


class Command(BaseCommand):
    """Waits for database will be available"""

    def handle(self, *args, **options):
        connection = connections["default"]
        db_up = False
        retry_count = 0
        max_retries = 3
        wait_time = 2
        while retry_count < max_retries and not db_up:
            try:
                connection.ensure_connection()
                db_up = True
                self.stdout.write(
                    self.style.SUCCESS("Database is running!")
                )
            except OperationalError:
                retry_count += 1
                self.stdout.write(self.style.WARNING(
                    f"Database unavailable! "
                    f"Attempt {retry_count}/{max_retries}. \n"
                    f"Retrying in {wait_time} seconds..."
                ))
                time.sleep(wait_time)
        if not db_up:
            self.stdout.write(self.style.ERROR(
                f"Unable to connect to the database after "
                f"{max_retries} attempts. Exiting."
            ))
            exit(1)
