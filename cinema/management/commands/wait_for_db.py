import time
import traceback

from django.core.management.base import BaseCommand
from django.db import connection
from django.db.utils import OperationalError


class Command(BaseCommand):
    def handle(self, *args, **options):
        db_ready = False
        while not db_ready:
            try:
                connection.ensure_connection()
                db_ready = True
            except OperationalError:
                traceback.print_exc()
                time.sleep(5)
