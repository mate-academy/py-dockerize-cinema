import time

from django.db import connection
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        db_conn = None
        while not db_conn:
            self.stdout.write("Waiting for database...")
            try:
                connection.ensure_connection()
                db_conn = True
            except OperationalError:

                time.sleep(2)

        self.stdout.write(self.style.SUCCESS("Database available!"))
