import time
from django.core.management import BaseCommand
from django.db import connection, OperationalError


class Command(BaseCommand):
    def handle(self, *args, **options):
        while True:
            try:
                cursor = connection.cursor()
                cursor.execute("SELECT 1")
                break
            except OperationalError:
                time.sleep(1)
