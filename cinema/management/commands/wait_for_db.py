import time

from django.core.management.base import BaseCommand, CommandError
from django.db import connections, OperationalError


class Command(BaseCommand):
    help = "Block until database is available or error after 10 seconds"

    def handle(self, *args, **options):
        for _ in range(10):
            try:
                connections["default"]
            except OperationalError:
                self.stdout.write("Waiting for database...")
                time.sleep(1)
            else:
                break
        else:
            raise CommandError("Database is not available after 10 seconds")
        self.stdout.write(self.style.SUCCESS("Database available!"))
