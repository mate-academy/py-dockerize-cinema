from time import sleep

from django.db import connection
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    """Waits for the DB connection"""

    def handle(self, *args, **options):
        sleep(5)
        try:
            connection.ensure_connection()
            print("Connection is ensured")
        except OperationalError:
            raise CommandError("Connection was not ensured")
