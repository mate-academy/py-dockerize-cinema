import time
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand
from django.db import connections


class Command(BaseCommand):
    """Django command to wait for the database to be available"""

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        db_conn = None
        while not db_conn:
            try:
                # Намагаємось отримати з"єднання за замовчуванням
                db_conn = connections["default"]
                # Спроба виконати будь-яку дію, щоб перевірити готовність
                db_conn.cursor()
            except OperationalError:
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available!"))
