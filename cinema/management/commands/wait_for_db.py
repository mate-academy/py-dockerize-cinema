import os
import time

from django.db import connection

from django.core.management.base import BaseCommand
from django.db.utils import OperationalError


class Command(BaseCommand):
    help = "Waiting for database will be available"

    def handle(self, *args, **options):
        max_second = 10
        while max_second > 0:
            try:
                connection.ensure_connection()
                break
            except OperationalError:
                time.sleep(1)
                max_second -= 1
                continue
