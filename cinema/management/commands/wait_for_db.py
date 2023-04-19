from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError
import time


class Command(BaseCommand):
    def handle(self, *args, **options) -> None:
        self.stdout.write("waiting for db connection")
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections["default"]
                self.stdout.write(self.style.SUCCESS("database is up!"))
            except OperationalError:
                self.stdout.write("database is not ready, retry in 1 second..")
                time.sleep(1)
