from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError
import time


class Command(BaseCommand):
    """ Django command to pause execution until database is available"""

    def handle(self, *args, **kwargs):
        self.stdout.write("waiting for db ...")
        db_conn = None
        while not db_conn:
            try:
                # get the database with keyword "default" from settings.py
                db_conn = connections["default"]

                with db_conn.cursor() as cursor:
                    cursor.execute("SELECT 1")
                    row = cursor.fetchone()

                    if row[0] == 1:
                        # prints success message in green
                        self.stdout.write(self.style.SUCCESS("db available"))

            except OperationalError:
                self.stdout.write(
                    "Database is unavailable, waiting 2 seconds ..."
                )
                time.sleep(2)
