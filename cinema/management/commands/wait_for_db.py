import time
from psycopg import OperationalError
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        """Entrypoint for command."""
        self.stdout.write("Waiting for database...")
        db_up = False

        while not db_up:
            try:
                self.check(databases=["default"])
                db_up = True
            except OperationalError:
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database ready!"))
