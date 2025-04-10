from django.core.management.base import BaseCommand
import psycopg2
import time
import os


class Command(BaseCommand):
    help = "Wait for the database to be available"

    def handle(self, *args, **kwargs):
        self.stdout.write("Waiting for database to be available...")
        while True:
            try:
                conn = psycopg2.connect(
                    dbname=os.environ.get("DB_NAME"),
                    user=os.environ.get("DB_USER"),
                    password=os.environ.get("DB_PASSWORD"),
                    host=os.environ.get("DB_HOST"),
                    port=os.environ.get("DB_PORT"),
                )
                conn.close()
                self.stdout.write(self.style.SUCCESS("Database is available"))
                break
            except psycopg2.OperationalError:
                self.stdout.write(
                    self.style.WARNING("Database not available, waiting...")
                )
                time.sleep(1)
