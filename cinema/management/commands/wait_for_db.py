from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        print("Waiting for database...")
        connection = None

        while not connection:
            try:
                connection = connections["default"]
                print("Database is ready...")
            except OperationalError:
                pass
