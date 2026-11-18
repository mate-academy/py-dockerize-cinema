import time

from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):

    def handle(self, *args, **options):
        print("waiting for database... ")
        while True:
            try:
                connections["default"].ensure_connection()
                break
            except OperationalError:
                time.sleep(1)

        print("Database available!")
