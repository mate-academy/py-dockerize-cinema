import time

from django.core.management import BaseCommand
from django.db import connections, OperationalError


class Command(BaseCommand):
    help = "Wait for db setting up and prevents app from running without db, timeout 15 sec"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Waiting for connection"))
        conn = None
        while not conn:
            try:
                conn = connections["default"]
            except OperationalError:
                self.stdout.write(self.style.WARNING(
                    "Retrying"
                ))
                time.sleep(1)
