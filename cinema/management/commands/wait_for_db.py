from django.core.management.base import BaseCommand
from django.db import connections, OperationalError
import time


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database")
        db = None
        while not db:
            try:
                db = connections["default"]
            except OperationalError:
                self.stdout.write("Database unavailable, waiting 1 second")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available!"))
