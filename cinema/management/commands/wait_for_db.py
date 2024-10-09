from time import sleep

from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.wait_for_db()

    def wait_for_db(self):
        self.stdout.write("Waiting for database...")
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections["default"]
                db_conn.ensure_connection()
                self.stdout.write(self.style.SUCCESS("Database available!"))
            except OperationalError:
                self.stdout.write("Database unavailable, waiting 1 second...")
                sleep(1)
