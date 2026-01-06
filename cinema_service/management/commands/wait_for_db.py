import time
from django.core.management.base import BaseCommand
from django.db.utils import OperationalError
from django.db import connections


class Command(BaseCommand):
    help = "Wait until db is available"

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        db_conn = None
        while db_conn is None:
            try:
                db_conn = connections["default"].cursor()
            except OperationalError:
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available"))
