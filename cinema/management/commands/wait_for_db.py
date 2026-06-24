import time

from django.core.management import BaseCommand
from django.db import OperationalError, connections


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")

        db_up = False
        while not db_up:
            try:
                with connections["default"].cursor():
                    db_up = True
            except OperationalError:
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available!"))
