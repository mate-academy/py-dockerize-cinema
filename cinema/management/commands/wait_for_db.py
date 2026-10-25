from time import sleep

from django.core.management.base import BaseCommand
from django.db import connection
from django.db.utils import OperationalError


class Command(BaseCommand):
    help = "Waiting for database"  # noqa: VNE003

    def handle(self, *args, **options):

        while True:
            try:
                connection.ensure_connection()
            except OperationalError:
                sleep(1)
            else:
                break

        self.stdout.write(
            self.style.SUCCESS("Database ready!")
        )
