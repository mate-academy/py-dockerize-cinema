import time as time_module
from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    help = "Waits for database to be available"

    def handle(self, *args, **kwargs):
        self.stdout.write("Waiting for database...")
        connected = False
        while not connected:
            try:
                connections["default"].cursor()
                connected = True
            except OperationalError:
                self.stdout.write("Database unavailable, waiting 1 second...")
                time_module.sleep(1)
        self.stdout.write(self.style.SUCCESS("Database available!"))
