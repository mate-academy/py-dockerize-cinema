from django.core.management.base import BaseCommand
from django.db import connections, OperationalError

from time import sleep


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("waiting for database...")
        while True:
            try:
                connections["default"].ensure_connection()
                self.stdout.write("database connected")
                break
            except OperationalError:
                sleep(1)
