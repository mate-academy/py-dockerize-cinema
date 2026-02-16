import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        self.stdout.write("Waiting for DataBase Up...")

        db_up = False

        while not db_up:
            try:
                connections["default"].cursor()
                db_up = True
            except (OperationalError):
                self.stdout.write("DataBase unavailable. Wait...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("DataBase is available now!!!"))
