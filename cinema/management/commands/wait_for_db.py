import time

from django.core.management import BaseCommand
from django.db import connections, OperationalError


class Command(BaseCommand):
    def handle(self, *args, **options):
        db_conn = None
        while not db_conn:
            try:
                connections["default"].cursor()
                db_conn = True
            except OperationalError:
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("DB is available!"))
