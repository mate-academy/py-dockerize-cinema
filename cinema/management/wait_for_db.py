import time

from django.core.management import BaseCommand
from django.db import connections, DEFAULT_DB_ALIAS


class Command(BaseCommand):
    """
    Command that waits for the database to become available.
    """

    def handle(self, *args, **options):
        """
        Repeatedly checks the database connection, waits if unavailable.
        """
        self.stdout.write("Waiting for database...")
        max_attempts = 5
        for attempt in range(max_attempts):
            connection = connections[DEFAULT_DB_ALIAS]
            if connection.ensure_connection():
                self.stdout.write(self.style.SUCCESS("Database available!"))
                return
            else:
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)

        self.stdout.write(self.style.ERROR(
            "Database unavailable after several attempts."
        ))
