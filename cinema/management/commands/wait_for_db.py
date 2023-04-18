from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        self.stdout.write("Waiting for database...")
        connection = None

        while not connection:
            try:
                connection = connections["default"]
                self.stdout.write(self.style.SUCCESS("Database available"))
            except OperationalError:
                pass
