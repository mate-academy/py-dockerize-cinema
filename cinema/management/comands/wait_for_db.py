from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError
import time


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        self.stdout.write("Wait when database ready")
        connection = None
        while not connection:
            try:
                connection = connections["default"]
                self.stdout.write(self.style.SUCCESS("Database is ready!"))
            except OperationalError:
                self.stdout.write("Database is not ready yet")
                time.sleep(1)
