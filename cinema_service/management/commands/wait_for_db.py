import time

from django.core.management.base import BaseCommand
from django.db import connections, OperationalError


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write("Waiting db...")
        db_conn = None
        while db_conn is None:
            try:
                db_conn = connections["default"]
            except OperationalError:
                self.stdout.write("Database starts...")
                time.sleep(1)

        self.stdout.write(
            self.style.SUCCESS("Database is available")
        )
