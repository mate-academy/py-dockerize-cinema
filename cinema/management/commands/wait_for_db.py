from time import sleep

from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


def log_db_wait(func):
    def wrapper(self, *args, **kwargs):
        self.stdout.write("Waiting for database...")
        result = func(self, *args, **kwargs)
        self.stdout.write(self.style.SUCCESS("Database available!"))
        return result
    return wrapper


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.wait_for_db()

    @log_db_wait
    def wait_for_db(self):
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections["default"]
                db_conn.ensure_connection()
            except OperationalError:
                self.stdout.write("Database unavailable, waiting 1 second...")
                sleep(1)
