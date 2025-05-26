from django.core.management.base import BaseCommand
import time
import psycopg2
from django.db import OperationalError


class Command(BaseCommand):
    help = "Waits for database..."

    def handle(self, *args, **kwargs):
        self.stdout.write("Waiting for database...")
        db_up = False
        while not db_up:
            try:
                conn = psycopg2.connect(
                    dbname='postgres',
                    user='postgres',
                    password='postgres',
                    host='db'
                )
                db_up = True
            except OperationalError:
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("Database is available!"))
