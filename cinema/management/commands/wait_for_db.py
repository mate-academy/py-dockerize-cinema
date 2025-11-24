from time import sleep

from django.core.management import BaseCommand
from django.db import connections, OperationalError


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("waiting for db...")
        db = False

        while not db:
            try:
                connections["default"].cursor()
                db = True
            except OperationalError:
                self.stdout.write("db connection failed..., retrying...")
                sleep(1)

        self.stdout.write("db connection succeeded...")
