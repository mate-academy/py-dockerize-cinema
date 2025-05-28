import time
from django.core.management.base import BaseCommand
from psycopg.errors import OperationalError
import psycopg


class Command(BaseCommand):
    help = "Waits for database to be available"

    def handle(self, *args, **kwargs):
        self.stdout.write("Waiting for database")
        while True:
            try:
                conn = psycopg.connect(
                    dbname="cinema",
                    user="cinema",
                    password="cinema",
                    host="db",
                    port="5432",
                )
                conn.close()
                self.stdout.write(self.style.SUCCESS("Database available!"))
                break
            except OperationalError as e:
                self.stdout.write(f"Database unavailable, error: {e}")
                self.stdout.write("Sleeping 1 second")
                time.sleep(1)
