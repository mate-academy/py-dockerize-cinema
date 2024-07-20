from time import sleep

from django.core.management.base import BaseCommand
from django.db import connection
from django.db.utils import OperationalError


ATTEMPT_NUMBER = 35
DELAY = 0.15


class Command(BaseCommand):
    help = "Wait for database container is up"

    def handle(self, **kwargs):
        attempt = 0
        while True:
            try:
                cursor = connection.cursor()
                cursor.close()
                break
            except OperationalError:
                if attempt < ATTEMPT_NUMBER:
                    attempt += 1
                    sleep(DELAY)
                    continue
                else:
                    self.stdout.write("Database is not accessable")
                    break
