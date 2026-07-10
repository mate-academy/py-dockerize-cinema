import time
from psycopg2 import OperationalError as Psycopg2OpError
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Czekam na bazę danych...")
        db_up = False
        while not db_up:
            try:
                self.check(databases=["default"])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write("Baza niedostępna, czekam 1 sekundę...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Baza danych gotowa!"))
