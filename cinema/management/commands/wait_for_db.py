import time

from django.core.management.base import BaseCommand
from django.db import connections
from psycopg import OperationalError


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS("Waiting for database...")
        )

        db_conn = None

        while not db_conn:
            try:
                connections["default"].ensure_connection()
                db_conn = True
            except OperationalError:
                self.stdout.write("Pls wait for connect to db")
                time.sleep(1)
        self.stdout.write("Success connection to db")
