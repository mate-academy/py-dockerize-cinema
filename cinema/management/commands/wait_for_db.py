from time import sleep
from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write("Waiting for db...")
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections["default"]
            except OperationalError:
                self.stdout.write("Waiting...")
                sleep(1)
        self.stdout.write(
            self.style.SUCCESS(
                "Database has been successfully connected"
            )
        )
