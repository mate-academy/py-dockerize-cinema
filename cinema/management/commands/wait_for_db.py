from time import sleep

from django.db import connection
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    """Waits for the DB connection"""

    def handle(self, *args, **options):
        connected = False
        while not connected:
            try:
                connection.ensure_connection()
                connected = True
                print("Connection to DB is ensured")
            except OperationalError:
                print("Connection is not ensured, trying again in 1 second...")
                sleep(1)
