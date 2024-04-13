import time

from django.core.management import BaseCommand
from django.db import connections
from psycopg import OperationalError


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        db_connect = None
        while not db_connect:
            try:
                db_connect = connections["default"]
            except OperationalError:
                self.stdout.write(self.style.ERROR("Unable to connect to database"))
                time.sleep(5)
        self.stdout.write(self.style.SUCCESS("Connected to database"))
