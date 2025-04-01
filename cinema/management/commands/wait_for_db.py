import os
from django.core.management.base import BaseCommand
from django.db import connections
from psycopg import OperationalError as PsycopgOperationalError
from django.db.utils import OperationalError
import time


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=["default"])
                db_up = True
            except (PsycopgOperationalError, OperationalError):
                self.stdout.write("Database is unavailable, waiting 1 second...") # noqa
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("Database is available"))
