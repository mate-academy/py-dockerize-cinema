import time

from django.core.management import BaseCommand
from django.db import connections
from psycopg import OperationalError


class Command(BaseCommand):
    def handle(self, *args, **options):

        while True:
            try:
                connections["default"].cursor()
                break
            except OperationalError:
                time.sleep(1)
