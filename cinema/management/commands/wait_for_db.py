import time

from django.core.management.base import BaseCommand
from django.db import connections, OperationalError


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Wait to connect to database...")
        db_conn = connections["default"]

        while True:
            try:
                db_conn.ensure_connection()
                break
            except OperationalError:
                self.stdout.write("Reconnect...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Success"))
