import time
from django.db import connections
from django.core.management.base import BaseCommand
from django.db.utils import OperationalError


class Command(BaseCommand):
    command_help = "Waits for the database to be available."

    def handle(self, *args, **kwargs):
        self.stdout.write("Waiting for database...")
        db_connect = None
        while not db_connect:
            try:
                db_connect = connections["default"]
                db_connect.ensure_connection()
            except OperationalError:
                self.stdout.write("Database unavailable. waiting 1 second...")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("Database available!"))
