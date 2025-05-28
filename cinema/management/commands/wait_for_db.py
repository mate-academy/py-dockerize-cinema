import time
from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    help = "Waits for database to be available"

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        connected  = None
        while not connected :
            try:
                connections["default"].cursor()
                connected  = True
            except OperationalError:
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("Database available!"))
