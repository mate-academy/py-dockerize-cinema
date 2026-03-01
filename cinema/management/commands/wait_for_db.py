import time
from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError
from psycopg2 import OperationalError as Psycopg2Error


class Command(BaseCommand):
    """Django command to wait for database to be available"""

    def handle(self, *args, **options):
        """Entrypoint for command - виконується при запуску команди"""

        self.stdout.write("Waiting for database...")
        db_up = False

        while not db_up:
            try:
                # Пробуємо отримати з'єднання з БД
                # Якщо БД не готова — викине одну з двох помилок нижче
                connections["default"].ensure_connection()
                db_up = True
            except (Psycopg2Error, OperationalError):
                # Psycopg2Error: БД ще не запустилась взагалі
                # OperationalError: БД запустилась але ще не приймає з'єднання
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)  # чекаємо 1 секунду і пробуємо знову

        # self.style.SUCCESS - виводить текст зеленим кольором в терміналі
        self.stdout.write(self.style.SUCCESS("Database available!"))
