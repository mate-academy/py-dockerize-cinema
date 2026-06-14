from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError
import time


class Command(BaseCommand):
    def handle(self, *args, **options):
        for _ in range(10):
            try:
                connections["default"].cursor()
                return
            except OperationalError:
                self.stdout.write("Connecting...")
                time.sleep(2)
        raise OperationalError("Connection failed")
