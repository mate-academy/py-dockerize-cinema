import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        success_connection = None
        while not success_connection:
            try:
                success_connection = connections["default"]
                success_connection.cursor()
            except OperationalError:
                time.sleep(1)
            finally:
                if success_connection:
                    success_connection.close()
