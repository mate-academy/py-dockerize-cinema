from django.core.management.base import BaseCommand
from django.db.utils import OperationalError
from django.db import connections


class Command(BaseCommand):

    def handle(self, *args, **options):
        connection = None
        self.stdout.write("Waiting db connection...")
        while not connection:
            try:
                connection = connections["default"]
                connection.cursor()
            except OperationalError:
                self.stdout.write("Please wait ...")
        self.stdout.write("Db is ready")
