import time

from django.core.management import BaseCommand
from psycopg2 import OperationalError
from psycopg2 import OperationalError as Psycopg2OpError


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write("Waiting for db")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=["default"])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)
        self.stdout.write("Database available")
