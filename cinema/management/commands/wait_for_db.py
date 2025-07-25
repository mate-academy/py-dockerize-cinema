import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Wait for database to be ready"

    def handle(self, *args, **kwargs):
        self.stdout.write("Waiting for database...")
        db_ready = False

        while not db_ready:
            try:
                connection = connections["default"]
                connection.cursor().close()
                db_ready = True
            except OperationalError:
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database is available!"))
