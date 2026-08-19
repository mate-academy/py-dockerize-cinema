import time
from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError
from psycopg2 import OperationalError as Psycopg2Error  # Якщо використовуєте PostgreSQL


class Command(BaseCommand):
    """Кастомна команда Django для очікування готовності бази даних."""

    def handle(self, *args, **options):
        self.stdout.write("Очікування бази даних...")
        db_up = False

        while not db_up:
            try:
                # Перевіряємо з'єднання з дефолтною БД
                connection = connections["default"]
                connection.cursor()
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write("База даних недоступна, чекаємо 1 секунду...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("База даних готова до роботи!"))
