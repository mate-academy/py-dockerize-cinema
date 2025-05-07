import time

from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django команда для очікування доступності бази даних"""

    def handle(self, *args, **options):
        self.stdout.write("Очікування підключення до бази даних...")
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections["default"].cursor()
            except OperationalError:
                self.stdout.write(
                    "База даних недоступна, очікування 1 секунду..."
                )
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("База даних доступна!"))
