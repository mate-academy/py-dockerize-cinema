import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    command_help = "Closes the specified poll for voting"

    def wait_for_db(self):
        db_connection = None
        while not db_connection:
            try:
                db_connection = connections["default"]
                db_connection.cursor()
            except OperationalError:
                print("Database connection failed.")
                time.sleep(1)

    def handle(self, *args, **kwargs):
        self.stdout.write("Waiting for database...")
        self.wait_for_db()
        self.stdout.write(self.style.SUCCESS("Database is ready!"))
