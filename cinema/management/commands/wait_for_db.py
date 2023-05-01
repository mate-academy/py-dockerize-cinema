from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError
import time


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        self.stdout.write("Waiting for DB ...")
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections["default"]
                self.stdout.write(self.style.SUCCESS("DB available"))
            except OperationalError:
                self.stdout.write("DB is not up, waiting ...")
                time.sleep(1)
