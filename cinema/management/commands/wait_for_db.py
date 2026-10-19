import time

from django.core.management import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    def handle(self, *args, **options):
        duration = 5
        start_time = time.time()
        db_conn = connections["default"]
        while time.time() - start_time < duration:
            try:
                db_conn.ensure_connection()
                break
            except OperationalError:
                time.sleep(1)
        else:
            raise OperationalError("Database did not connect in time")
