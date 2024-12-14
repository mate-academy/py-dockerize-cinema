from time import sleep

from django.core.management import BaseCommand
from django.db import connections, OperationalError


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("waiting for db...")
        db_connection = None

        while not db_connection:
            try:
                db_connection = connections["default"]
            except OperationalError:
                self.stdout.write(
                    "db not available yet, reconnecting in 1 second"
                )
                sleep(1)
        self.stdout.write("db available")
