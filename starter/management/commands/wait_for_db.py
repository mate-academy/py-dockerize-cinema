import time
from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        self.stdout.write("Waiting for database...")
        try_counter = 0
        max_retries = 40

        while True:
            try:
                db_conn = connections["default"]
                db_conn.cursor()

                self.stdout.write(self.style.SUCCESS("Database connected!"))
                break

            except OperationalError:
                self.stdout.write(
                    "Database unavailable, waiting 2 seconds..."
                )
                time.sleep(2)
                try_counter += 1

            if try_counter >= max_retries:
                self.stdout.write(
                    self.style.ERROR("Cannot connect to db!"
                                     " Check your connection or"
                                     " try again later.!")
                )
                raise Exception("Database not available")
