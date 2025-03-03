from time import sleep
from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Waiting for the database...")
        db_up = False
        while not db_up:
            try:
                connection = connections["default"]
                connection.cursor()
                db_up = True
            except OperationalError:
                self.stdout.write("Database unavailable, waiting 5 seconds...")
                sleep(5)
        self.stdout.write(self.style.SUCCESS("The database is available!"))
