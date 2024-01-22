from time import sleep

from django.core.management import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write("Waiting for db...")
        db_connection = None
        while not db_connection:
            try:
                db_connection = connections["default"]
            except OperationalError:
                self.stdout.write("Waiting...")
                sleep(1)
        self.stdout.write(
            self.style.SUCCESS(
                "Database has been successfully connected"
            )
        )
