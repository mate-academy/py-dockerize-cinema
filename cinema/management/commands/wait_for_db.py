import time

from django.core.management import BaseCommand
from django.db import connections, OperationalError


class Command(BaseCommand):
    def handle(self, *args, **options):
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections["default"]
                db_conn.cursor()
            except OperationalError:
                time.sleep(1)
