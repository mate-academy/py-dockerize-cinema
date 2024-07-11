import time

from django.core.management.base import BaseCommand
from django.db import connection, OperationalError


class Command(BaseCommand):
    def handle(self, *args, **options) -> None:
        self.stdout.write("Connection to db...")
        db_connection = None
        while db_connection:
            try:
                db_connection = connection["default"]
            except OperationalError:
                self.stdout.write("Connection failed, trying to reconnect")
                time.sleep(1)

        self.stdout.write("DB connected successfully")
