import time

from django.core.management.base import BaseCommand
from django.db import connections, OperationalError


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database connection ...")
        db_conn = False
        while not db_conn:
            try:
                db_conn = connections["default"]
            except OperationalError:
                self.stdout.write("Database is unavailable, please wait ...")
                time.sleep(3)

        self.stdout.write(self.style.SUCCESS("Successfully connected"))
