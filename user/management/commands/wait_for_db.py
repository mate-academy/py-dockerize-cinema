from django.core.management.base import BaseCommand, CommandError
from django.db import connections
from django.db.utils import OperationalError
from time import sleep


class Command(BaseCommand):
    """Waits for the database to be available"""

    def handle(self, *args, **options):
        while not self.check_database():
            sleep(5)
            self.stdout.write(
                self.style.WARNING("Database unavailable, waiting 5 second...")
            )

    @staticmethod
    def check_database():
        db_conn = connections["default"]
        try:
            db_conn.cursor()
        except OperationalError:
            return False
        return True
