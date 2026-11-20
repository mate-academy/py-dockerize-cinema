import time

from django.core.management.base import BaseCommand, CommandError
from django.db import OperationalError, connection


class Command(BaseCommand):
    help = "Wait until the database is available."  # noqa: VNE003
    requires_system_checks = []

    def handle(self, *args, **options):
        max_attempts = 30
        self.stdout.write("Waiting for db")

        for attempt in range(1, max_attempts + 1):
            try:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT 1")
            except OperationalError as error:
                connection.close()

                if attempt == max_attempts:
                    raise CommandError(
                        f"Database unavailable after {max_attempts}"
                        f" attempts: {error}"
                    ) from error

                self.stdout.write(
                    f"Attempt {attempt}/{max_attempts} failed. "
                    f"Retrying in 1 second"
                )
                time.sleep(1)
            else:
                self.stdout.write(self.style.SUCCESS("Database is available!"))
                return
