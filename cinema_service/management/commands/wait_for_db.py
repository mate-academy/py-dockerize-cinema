from django.core.management.base import BaseCommand
import time
import psycopg2
from django.db import connections
from django.db.utils import OperationalError
class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Waiting for database...')
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
                c = db_conn.cursor()
                c.execute('SELECT 1')
            except OperationalError:
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database available!'))
