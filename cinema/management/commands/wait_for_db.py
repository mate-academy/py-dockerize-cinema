import time
from django.core.management.base import BaseCommand
from django.db.utils import OperationalError
from django.db import connections
from dotenv import load_dotenv

load_dotenv()


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Try connection Database")
        connection_db = None
        meter = 0
        while not connection_db:
            try:
                connection_db = connections["default"]
            except OperationalError:
                self.stdout.write("Database not connected, need wait.")
            time.sleep(1)
            meter += 1
            if meter == 30:
                assert OperationalError
        self.stdout.write(self.style.SUCCESS("Database available!"))
