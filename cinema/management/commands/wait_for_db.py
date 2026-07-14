import time
import sys
from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Очікування доки база даних не стане доступною"  # noqa: VNE003

    def handle(self, *args, **options):
        self.stdout.write("Очікування бази даних...")
        db_conn = None
        max_retries = 30
        retries = 0

        while not db_conn and retries < max_retries:
            try:
                db_conn = connections["default"]
                db_conn.cursor()
            except OperationalError:
                retries += 1
                self.stdout.write(
                    f"База даних недоступна, очікування 1 сек... "
                    f"(Спроба {retries}/{max_retries})"
                )
                time.sleep(1)

        if db_conn:
            self.stdout.write(self.style.SUCCESS("База даних доступна!"))
        else:
            self.stdout.write(
                self.style.ERROR("Перевищено час очікування БД. Вихід...")
            )
            sys.exit(1)
