import time

from django.core.management import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Waiting for response from database")
        db_conn = None
        attempts = 30
        while not db_conn and attempts != 0:
            attempts -= 1
            try:
                db_conn = connections["default"]
            except OperationalError:
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(2)

        self.stdout.write(self.style.SUCCESS("Database available!"))
