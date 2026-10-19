import time
from django.core.management.base import BaseCommand
from django.db import connection
from django.db.utils import OperationalError


class Command(BaseCommand):
    def handle(self, *args, **options):
        for _ in range(30):
            try:
                connection.ensure_connection()
                self.stdout.write(self.style.SUCCESS("Database is ready!"))
                return
            except OperationalError:
                time.sleep(2)

        self.stderr.write(self.style.ERROR("Database unavailable."))
        exit(1)
