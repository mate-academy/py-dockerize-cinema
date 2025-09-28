import time

from django.core.management import CommandError
from django.core.management.base import BaseCommand
from django.db import connections, OperationalError


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        db_conn = None
        counter = 0
        while not db_conn and counter < 60:
            try:
                db_conn = connections["default"]
                db_conn.cursor()
            except OperationalError:
                counter += 1
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)
        if db_conn:
            self.stdout.write(self.style.SUCCESS("Database available!"))
        else:
            self.stdout.write(self.style.ERROR(
                "Database unavailable after 5 retries!")
            )
            raise CommandError("Database unavailable!")
