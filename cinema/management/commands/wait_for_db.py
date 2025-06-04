import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to pause execution until database is available."""

    def handle(self, *args, **options):
        self.stdout.write('Waiting for database...')
        db_conn = None
        attempt = 0

        while not db_conn:
            try:
                db_conn = connections['default']
                db_conn.cursor()
            except OperationalError:
                attempt += 1
                self.stdout.write(self.style.WARNING(
                    f'Database unavailable,'
                    f' waiting 1 second... (attempt {attempt})'))
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))
