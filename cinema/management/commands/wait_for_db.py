import time
from django.core.management.base import BaseCommand
from django.db.utils import OperationalError


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Waiting for db connection...")
        db_up = False
        while not db_up:
            try:
                self.check(databases=["default"])
            except OperationalError:
                self.stdout.write("Database unavailable, waiting...")
                time.sleep(1)
            else:
                db_up = True
        self.stdout.write(self.style.SUCCESS("Database connected!"))
