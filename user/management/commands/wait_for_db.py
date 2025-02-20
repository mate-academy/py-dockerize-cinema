import time
import os
import psycopg2
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        while True:
            try:
                conn = psycopg2.connect(
                    dbname=os.getenv("POSTGRES_NAME"),
                    user=os.getenv("POSTGRES_USER"),
                    password=os.getenv("POSTGRES_PASSWORD"),
                    host=os.getenv("POSTGRES_HOST"),
                    port=os.getenv("POSTGRES_PORT"),
                )
                conn.close()
                break
            except psycopg2.OperationalError:
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available!"))
