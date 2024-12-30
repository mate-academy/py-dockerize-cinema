import os
import time
import psycopg2
from django.core.management.base import BaseCommand
from django.db.utils import OperationalError


class Command(BaseCommand):
    help = "Waits for the database to be available..."

    def handle(self, *args, **kwargs):
        self.stdout.write("Check database...")

        while True:
            try:
                with psycopg2.connect(
                    dbname=os.environ["POSTGRES_NAME"],
                    user=os.environ["POSTGRES_USER"],
                    password=os.environ["POSTGRES_PASSWORD"],
                    host=os.environ["POSTGRES_HOST"],
                    port=os.environ["POSTGRES_PORT"],
                ) as conn:
                    self.stdout.write(
                        self.style.SUCCESS("Database is available")
                    )
                    break
            except OperationalError:
                self.stdout.write("The database is not available, waiting")
                time.sleep(1)
