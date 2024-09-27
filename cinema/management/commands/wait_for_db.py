import os
import time
import psycopg2
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Waiting for the database...")

        db_ready = False
        while not db_ready:
            try:
                connection = psycopg2.connect(
                    dbname=os.environ["POSTGRES_DB"],
                    user=os.environ["POSTGRES_USER"],
                    password=os.environ["POSTGRES_PASSWORD"],
                    host=os.environ["POSTGRES_HOST"],
                )
                connection.close()
                db_ready = True
            except psycopg2.OperationalError:
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database is available!"))
