import time

from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    help = "Wait for database"  # noqa: VNE003

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        db_up = False
        count = 0
        max_tries = 10
        while db_up is False and count < max_tries:
            try:
                with connections["default"].cursor() as cursor:
                    cursor.execute("SELECT 1;")
                db_up = True
            except OperationalError:
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)
                count += 1

        self.stdout.write(self.style.SUCCESS("Database ready!"))
