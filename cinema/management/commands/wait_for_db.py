from time import sleep

from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):

    def handle(self, *args, **options):
        while True:
            try:
                connections["default"].ensure_connection()
                return
            except OperationalError:
                sleep(1)
