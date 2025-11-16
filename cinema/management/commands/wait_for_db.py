import time
from django.core.management.base import BaseCommand
from django.db import OperationalError, connections


class Command(BaseCommand):
    help_text = "Waits for the database to be available"

    def handle(self, *args, **kwargs):
        while True:
            try:
                db = connections["default"]
                db.cursor()
                self.stdout.write(self.style.SUCCESS("Database available"))
                break
            except OperationalError:
                self.stdout.write("Database unavailable, wait")
                time.sleep(1)
