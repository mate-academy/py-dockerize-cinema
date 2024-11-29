import time

from django.core.management import BaseCommand
from django.db import connections
from psycopg2 import OperationalError


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Waiting for db to start", ending="\n")
        db = None
        attempts = 5
        while not db and attempts > 0:
            try:
                db = connections["default"]
                self.stdout.write(self.style.SUCCESS("Connected to db"))
            except OperationalError:
                attempts -= 1
                self.stdout.write("DB is unavailable, try again in 1 second..")
                time.sleep(1)
        if not db:
            self.stdout.write(self.style.ERROR("Not connected to db"))
            raise OperationalError("DB is unavailable")
