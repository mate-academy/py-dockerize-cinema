import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        db_connection = None
        while not db_connection:
            try:
                db_connection = connections["default"]
            except OperationalError:
                time.sleep(3)
