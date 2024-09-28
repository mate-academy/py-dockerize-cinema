import time

from django.core.management.base import BaseCommand
from django.db import connections, OperationalError


class Command(BaseCommand):
    help = "Provides correct composing between app and Data base"

    def wait_for_db(self, *args, **kwargs):
        db_connection = None
        while not db_connection:
            try:
                connection = connections["default"]
                connection.cursor()
            except OperationalError:
                time.sleep(1)

        self.stdout.write(
            self.style.SUCCESS("Successfully connected to database")
        )
