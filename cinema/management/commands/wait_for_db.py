import time
from django.db import connections
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Waiting for DB to start")
        connection = None
        while not connection:
            try:
                connection = connections["default"]
            except CommandError:
                self.stdout.write("Database is unavailable, waiting...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database is up!"))
