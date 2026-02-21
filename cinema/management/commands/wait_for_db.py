import time
from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    def handle(self, *args, **options):
        while True:
            try:
                connections["default"].cursor()
                break
            except OperationalError:
                self.stdout.write("Waiting for DB...")
                time.sleep(1)
