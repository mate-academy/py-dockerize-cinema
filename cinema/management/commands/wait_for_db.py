import time
from django.db import connections as connect
from django.db.utils import OperationalError
from django.core.management import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write("Checking DB ready", ending="")
        db_connect = connect["default"]
        while not db_connect:
            try:
                db_connect = connect["default"]
            except OperationalError:
                self.stdout.write("Error", ending="")
                time.sleep(1)
        self.stdout.write("\nReady")
