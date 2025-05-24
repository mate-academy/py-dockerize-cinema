import time
from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    """Django command to wait for database availability"""

    def handle(self, *args, **options):
        self.stdout.write('Checking database connection...')
        max_retries = 30
        retry_delay = 1  # second

        for attempt in range(1, max_retries + 1):
            try:
                db_conn = connections['default']
                db_conn.ensure_connection()
                self.stdout.write(self.style.SUCCESS('Database available!'))
                return
            except OperationalError:
                if attempt < max_retries:
                    self.stdout.write(
                        f'Attempt {attempt}/{max_retries}: Database unavailable, '
                        f'waiting {retry_delay} sec...'
                    )
                    time.sleep(retry_delay)
                else:
                    self.stdout.write(
                        self.style.ERROR(
                            f'Could not connect to database after {max_retries} attempts'
                        )
                    )
                    raise
