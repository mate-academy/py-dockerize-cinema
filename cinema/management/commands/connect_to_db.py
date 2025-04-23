import time

from django.core.management.base import BaseCommand
from psycopg2 import OperationalError
from django.db import connections


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Connecting to DB")

        connected = False

        while not connected:
            try:
                connection = connections["default"]
                with connection.cursor() as cursor:
                    cursor.execute("SELECT 1")
                connected = True
                self.stdout.write("Connected to DB successfully")
            except OperationalError:
                self.stdout.write("Connecting to DB failed")
                time.sleep(1)
