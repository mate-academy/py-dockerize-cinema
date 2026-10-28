import os
import time
from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    help = "Wait for database to be available"

    def handle(self, *args, **options):
        max_retries = int(os.getenv("DB_WAIT_MAX_RETRIES", "60"))
        delay = float(os.getenv("DB_WAIT_DELAY", "1"))

        self.stdout.write(self.style.WARNING("Waiting "
                                             "for database..."))
        ready = False
        retries = 0

        while not ready and retries < max_retries:
            try:
                connections["default"].cursor()
                ready = True
            except OperationalError as exc:
                retries += 1
                self.stdout.write(f"DB unavailable ({exc}), "
                                  f"retry {retries}; sleep {delay}s")
                time.sleep(delay)

        if not ready:
            self.stderr.write(self.style.ERROR("Database "
                                               "is not "
                                               "available after retries"))
            raise SystemExit(1)

        self.stdout.write(self.style.SUCCESS("Database is available!"))
