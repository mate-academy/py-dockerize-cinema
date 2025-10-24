import time

from django.core.management.base import BaseCommand
from django.db import connection
from django.db.utils import OperationalError


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Wait for db connection")
        db_up = False
        while not db_up:
            try:
                connection.ensure_connection()
                db_up = True
            except OperationalError:
                self.stdout.write("db unavailable")
                time.sleep(5)
        self.stdout.write(self.style.SUCCESS("db is ready "))
