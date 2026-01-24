from django.core.management.base import BaseCommand
from django.db.utils import OperationalError
import time


class Command(BaseCommand):
    help = "Wait for database to be available"    # noqa: VNE003

    def handle(self, *args, **kwargs):
        self.stdout.write("Waiting for database...")
        db_up = False
        while db_up is False:
            try:
                from django.db import connections

                connections["default"].cursor()
                db_up = True
            except OperationalError:
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database is available!"))
