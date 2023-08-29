import time

from django.core.management import BaseCommand
from django.db.utils import OperationalError
from django.db import connections


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Waiting for connection ...")
        db_conn = None

        while not db_conn:
            try:
                db_conn = connections["default"].cursor()
            except OperationalError:
                self.stdout.write("Database unavailable, waiting 2 seconds...")
                time.sleep(2)

        self.stdout.write(self.style.SUCCESS("Database available"))
