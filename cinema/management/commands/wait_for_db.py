import time

from django.core.management import BaseCommand
from django.db import connections, OperationalError


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write("waiting for db...")

        while True:
            try:
                connection = connections["default"]
                connection.cursor()
                break
            except OperationalError:
                self.stdout.write("Database connection failed.")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("Database connected."))
