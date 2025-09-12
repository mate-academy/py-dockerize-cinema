from django.core.management import BaseCommand
from django.db import connections
from django.db.utils import OperationalError
from time import sleep


class Command(BaseCommand):

    def handle(self, *args, **options):

        while True:
            self.stdout.write("waiting for database...")
            try:
                db_conn = connections["default"]
                db_conn.cursor()
                self.stdout.write(self.style.SUCCESS("Connected!"))
                break
            except OperationalError:
                self.stdout.write("Database unavailable, waiting 1 second...")
                sleep(1)
