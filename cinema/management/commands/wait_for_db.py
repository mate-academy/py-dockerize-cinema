from django.core.management import BaseCommand
from django.db.utils import OperationalError
from django.db import connections

import time


class Command(BaseCommand):
    MAX_RETRIES = 10
    RETRY_INTERVAL = 1

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        db_conn = None
        retries = 0
        while retries < self.MAX_RETRIES:
            try:
                db_conn = connections["default"]
            except OperationalError:
                self.stdout.write("Database unavailable, waiting...")
                time.sleep(self.RETRY_INTERVAL)
                retries += 1

        if db_conn:
            self.stdout.write(self.style.SUCCESS("Database is available!"))
        else:
            self.stdout.write(self.style.ERROR("Failed to connect to the "
                                               "database after "
                                               f"{self.MAX_RETRIES}"))
