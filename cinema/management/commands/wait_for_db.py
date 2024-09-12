import time

from django.core.management import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    """ Django command to pause execution until database is available"""
    def handle(self, *args, **kwargs):
        self.stdout.write("Waiting for DB")
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections["default"]

                self.stdout.write(self.style.SUCCESS("DB is available"))
            except OperationalError:
                self.stdout.write("Database unavailable, waiting 1 second")
                time.sleep(1)
