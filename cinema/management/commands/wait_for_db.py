import time

from django.core.management import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    def handle(self, *args: any, **options: any) -> None:
        self.stdout.write("Connection database")
        connection = None
        while not connection:
            try:
                connection = connections["default"].cursor()
            except OperationalError:
                self.stdout.write("Database unavailable")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database connected"))
