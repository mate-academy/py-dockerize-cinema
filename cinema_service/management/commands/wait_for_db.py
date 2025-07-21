import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Подождите, пока база данных станет доступной"

    def handle(self, *args, **kwargs):
        self.stdout.write("Жду базу данных...")
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections["default"]
                db_conn.cursor()
            except OperationalError:
                self.stdout.write("База данных недоступна, ожидание 1 секунда...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("База данных доступна!"))
