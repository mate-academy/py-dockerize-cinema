import time

from django.core.management.base import BaseCommand, CommandError
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):

    def handle(self, *args, **options):

        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
                db_conn.cursor()
            except OperationalError:
                self.stdout.write(self.style.WARNING('База данных не готова, ожидаем...'))
                time.sleep(1)
