import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    help = "Wait for db connection"  # noqa: VNE003

    def handle(self, *args, **options):
        self.stdout.write("Waiting for db connection...")
        db_conn = None
        while not db_conn:
            try:
                connections["default"].cursor()
                db_conn = True
            except OperationalError:
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("db connection established"))
