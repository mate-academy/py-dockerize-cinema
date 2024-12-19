import time

from django.core.management.base import BaseCommand
from django.db import connections, OperationalError


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        while True:
            try:
                connections["default"].ensure_connection()
                break
                print("Server loading...")
            except OperationalError:
                time.sleep(1)
