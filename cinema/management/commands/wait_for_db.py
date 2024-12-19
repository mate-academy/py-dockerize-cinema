import time

from django.core.management import BaseCommand
from django.db import connections, OperationalError


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        self.stdout.write("connecting to db")
        connection = None
        while not connection:
            try:
                connection = connections["default"]
                connection.cursor()
            except OperationalError as e:
                self.stdout.write(f"{e}, trying again")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("db available!"))
