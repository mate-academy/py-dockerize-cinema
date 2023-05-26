import time

from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    """This Django command to pause execution of application
            until database is available"""

    def handle(self, *args, **options):
        self.stdout.write("Waiting before db start...")
        db_connection = None
        while not db_connection:
            try:
                db_connection = connections["default"]
                self.stdout.write(
                    self.style.SUCCESS("Everything is OK, db is available")
                )
            except OperationalError:
                self.stdout.write("Database is unavailable, please wait ...")
                time.sleep(3)
