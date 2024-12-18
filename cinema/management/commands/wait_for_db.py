import time

from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        db_connection = None
        while not db_connection:
            try:
                db_connection = connections["default"]
                db_connection.cursor()
            except OperationalError:
                self.stdout.write(
                    self.style.WARNING(
                        "db connection failed, newxt try in 1 second"
                    )
                )
                time.sleep(1)
