import time

from django.core.management.base import BaseCommand
from django.db import connection
from django.db.utils import OperationalError


class Command(BaseCommand):

    def handle(self, *args, **options):
        while True:
            try:
                connection.ensure_connection()
            except OperationalError:
                self.stdout.write(
                    "Failed to find database"
                )
                time.sleep(5)
            else:
                break

        self.stdout.write(self.style.ERROR("Database found!"))
