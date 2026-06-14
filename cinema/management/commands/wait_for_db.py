from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError
import time


class Command(BaseCommand):
    def handle(self, *args, **options):
        while True:
            try:
                connections["default"].cursor()
                break
            except OperationalError:
                time.sleep(1)
