from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError

import time


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        db = None
        while db is None:
            try:
                db = connections["default"]
                db.cursor()
            except OperationalError:
                self.stdout.write("Database unavailable...")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("Database available"))
