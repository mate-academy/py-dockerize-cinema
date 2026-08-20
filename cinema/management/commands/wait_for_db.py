import time
from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError
from psycopg2 import OperationalError as Psycopg2Error


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write("Waiting for DB..")
        db_up = False

        while not db_up:
            try:
                connection = connections["default"]
                connection.cursor()
                db_up = True
            except (Psycopg2Error, OperationalError, OSError):
                self.stdout.write(
                    "The database is unavailable, please wait a moment..."
                )
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("The database is ready for use!"))
