from django.core.management import BaseCommand
from django.db import connections
from django.db.utils import OperationalError
import time


class Command(BaseCommand):

    def handle(self, *args, **options):
        tries = 0
        max_tries = 40
        while max_tries > tries:
            try:
                connections["default"].cursor()
                break
            except OperationalError:
                time.sleep(1)
            tries += 1
        self.stdout.write("Database available")
