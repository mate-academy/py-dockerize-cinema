import time

from django.core.management.base import BaseCommand, CommandError
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Waiting for database")
        connect = None
        while not connect:
            try:
                connect = connections["default"]
                connect.cursor()
            except OperationalError:
                time.sleep(1)

        self.stdout.write("Database connected")
