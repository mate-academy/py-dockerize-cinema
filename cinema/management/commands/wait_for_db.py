from django.core.management.base import BaseCommand
from django.db.utils import OperationalError
from django.db import connections
import time


class Command(BaseCommand):
    help_ = "Waits for db before starting the server"

    def handle(self, *args, **options):
        connection = connections["default"]
        while True:
            try:
                connection.is_usable()
                break
            except OperationalError:
                self.stdout.write(
                    self.style.WARNING("Waiting")
                )
                time.sleep(0.2)
        self.stdout.write(
            self.style.SUCCESS("No more sleeping")
        )
