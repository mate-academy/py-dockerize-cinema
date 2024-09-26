import time
from django.core.management.base import BaseCommand
from django.db.utils import OperationalError
from django.db import connections
from dotenv import load_dotenv

load_dotenv()


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        while True:
            try:
                connections["default"].cursor()
                break
            except OperationalError:
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available!"))
