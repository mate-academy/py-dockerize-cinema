from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand
import time


class Command(BaseCommand):
    def handle(self, *args, **options):
        db_up = False
        while not db_up:
            try:
                db_conn = connections["default"]
                db_conn.cursor()
                db_up = True
            except OperationalError:
                time.sleep(1)
